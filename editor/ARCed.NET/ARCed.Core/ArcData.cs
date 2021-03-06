﻿#region Using Directives

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;

#endregion

namespace ARCed
{
	/// <summary>
	/// Wrapper for standard Dictionary with dynamic key-value pairs
	/// </summary>
	public class Hash : Dictionary<dynamic, dynamic>
	{
		public dynamic GetKey(dynamic value)
		{
			return Keys.FirstOrDefault(key => value == this[key]);
		}
	}

	/// <summary>
    /// Wrapper for a Dictionary containing name-type pairs
	/// </summary>
	public class TypeMap : Dictionary<string, Type> { }

	/// <summary>
	/// Static class for serialization of .arc format
	/// </summary>
	public static class ArcData
	{

		/// <summary>
		/// Enum representing flags for type-identifying byte markers 
		/// </summary>
		public enum RubyTypes
		{
			/// <summary>
			/// Byte marker for NilClass value: 0x10 (16)
			/// </summary>
			NilClass = 0x10,
			/// <summary>
			/// Byte marker for FalseClass value: 0x11 (17)
			/// </summary>
			FalseClass = 0x11,
			/// <summary>
			/// Byte marker for TrueClass value: 0x12 (18)
			/// </summary>
			TrueClass = 0x12,
			/// <summary>
			/// Byte marker for Fixnum value: 0x21 (33)
			/// </summary>
			Fixnum = 0x21,
			/// <summary>
			/// Byte marker for Bignum value: 0x22 (34)
			/// </summary>
			Bignum = 0x22,
			/// <summary>
			/// Byte marker for Float value: 0x23 (35)
			/// </summary>
			Float = 0x23,
			/// <summary>
			/// Byte marker for String value: 0x30 (48)
			/// </summary>
			String = 0x30,
			/// <summary>
			/// Byte marker for Array value: 0x40 (64)
			/// </summary>
			Array = 0x40,
			/// <summary>
			/// Byte marker for Hash value: 0x41 (65)
			/// </summary>
			Hash = 0x41,
			/// <summary>
			/// Byte marker for Object value: 0x00 (0)
			/// </summary>
			Object = 0x00
		}

		#region Constants

		const string HEADER = "\x41\x52\x43\x44";  // ARCD
		const string VERSION = "\x01\x00";         // 1.0

		#endregion

		#region Private Fields

		private static Stream _stream = Stream.Null;
		private static List<dynamic> _strings = new List<dynamic> { null };
		private static List<dynamic> _arrays = new List<dynamic> { null };
		private static List<dynamic> _hashes = new List<dynamic> { null };
		private static List<dynamic> _objects = new List<dynamic> { null };
		private static TypeMap _mappedTypes;
		private static TypeMap _assemblyTypes;

		#endregion

		#region Public Methods

		/// <summary>
		/// Serializes the given object and writes it to the stream
		/// </summary>
		/// <param name="stream">IO stream to write to</param>
		/// <param name="obj">Object to write</param>
		public static void Dump(Stream stream, object obj)
		{
			Reset();
			_mappedTypes = new TypeMap();
			_stream = stream;
			_stream.Write(HEADER.GetBytes(), 0, 4);
			_stream.Write(VERSION.GetBytes(), 0, 2);
			try { ArcDump(obj); }
			finally { Reset(); }
		}

		/// <summary>
		/// Loads an object from the stream
		/// </summary>
		/// <param name="stream">Stream to read</param>
		/// <param name="assemblies">Assemblies that will be searched for known types</param>
		/// <returns>Deserialized object</returns>
		public static object Load(Stream stream, params Assembly[] assemblies)
		{
			var map = new TypeMap();
			foreach (var type in assemblies.SelectMany(assembly => assembly.GetTypes()))
			    map[type.ToString()] = type;
			return Load(stream, map);
		}

		/// <summary>
		/// Loads an object from the stream
		/// </summary>
		/// <param name="stream">Stream to read</param>
		/// <param name="assemblyTypes">Dictionary map for containing known types</param>
		/// <returns>Deserialized object</returns>
		public static object Load(Stream stream, TypeMap assemblyTypes)
		{
			_stream = stream;
			CheckHeader();
			_assemblyTypes = assemblyTypes;
			_mappedTypes = new TypeMap();
		    object data;
            try { data = ArcLoad(); }
			finally { Reset(); }
			return data;
		}

		#endregion

		#region Private Methods

		/// <summary>
		/// Checks formatting of header and version data at the beginning of the stream
		/// </summary>
		/// <exception cref="InvalidDataException">Thrown if header and version do not match proper format</exception>
		private static void CheckHeader()
		{
			_stream.Seek(0, SeekOrigin.Begin);
			string header = _stream.ReadByteString(4);
			if (header != HEADER)
			{
				string msg = String.Format("Incorrect header information. Looking for\"{0}\", found: \"{1}\"",
					HEADER, header);
				throw new InvalidDataException(msg);
			}
			string version = _stream.ReadByteString(2);
			if (version != VERSION)
			{
				string msg = String.Format("Incorrect version information. Looking for\"{0}\", found: \"{1}\"",
					VERSION, version);
				throw new InvalidDataException(msg);
			}
		}

		/// <summary>
		/// Closes the stream if open, and clears all mappings
		/// </summary>
		private static void Reset()
		{
			if (_stream != null)
				_stream.Dispose();
			_stream = Stream.Null;
			_strings.Clear();
			_strings.Add(null);
			_arrays.Clear();
			_arrays.Add(null);
			_hashes.Clear();
            _hashes.Add(null);
			_objects.Clear();
			_objects.Add(null);
		}

		/// <summary>
		/// Identifies the object type and dumps it to the stream accordingly
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void ArcDump(object obj)
		{
			if (obj == null) DumpNilClass();
			else if (obj is bool)
			{
				if ((bool)obj) DumpTrueClass();
				else DumpFalseClass();
			}
			else if (IsRubyFixnum(obj)) DumpFixnum(obj);
			else if (IsRubyBignum(obj)) DumpBignum(obj);
			else if (IsRubyFloat(obj)) DumpFloat(obj);
			else if (obj is String) DumpString(obj);
			else if (obj is Array) DumpArray(obj);
			else if (obj is DictionaryBase) DumpHash(obj);
			else
			{
				try { DumpObject(obj); }
				catch
				{
					string msg = String.Format("Objects of type \"{0}\" cannot be dumped.", obj.GetType());
					throw new SerializationException(msg);
				}
			}
		}

		/// <summary>
		/// Reads the type identifying byte marker from the current stream position, and loads the data accordingly
		/// </summary>
		/// <returns>Deserialized object</returns>
		private static dynamic ArcLoad()
		{
			var type = (RubyTypes)_stream.ReadByte();
			switch (type)
			{
				case RubyTypes.NilClass:   return LoadNilClass();
				case RubyTypes.FalseClass: return LoadFalseClass();
				case RubyTypes.TrueClass:  return LoadTrueClass();
				case RubyTypes.Fixnum:     return LoadFixnum();
				case RubyTypes.Bignum:     return LoadBignum();
				case RubyTypes.Float:      return LoadFloat();
				case RubyTypes.String:     return LoadString();
				case RubyTypes.Array:      return LoadArray();
				case RubyTypes.Hash:       return LoadHash();
				case RubyTypes.Object:     return LoadObject();
			}
			string msg = String.Format("Unknown byte identifier: {0}", type);
			throw new TypeLoadException(msg);
		}

		/// <summary>
		/// Checks an object if it us a numerical type falling in range of a Ruby Fixnum
		/// </summary>
		/// <param name="value">Object to check</param>
		/// <returns>Flag if object is Fixnum or not</returns>
		private static bool IsRubyFixnum(object value)
		{
			if (value is sbyte) return true;
			if (value is byte) return true;
			if (value is short) return true;
			if (value is ushort) return true;
			if (value is int) return true;
			return value is uint;
		}

		/// <summary>
		/// Checks an object if it us a numerical type falling in range of a Ruby Bignum
		/// </summary>
		/// <param name="value">Object to check</param>
		/// <returns>Flag if object is Bignum or not</returns>
		private static bool IsRubyBignum(object value)
		{
			if (value is long) return true;
			return value is ulong;
		}

		/// <summary>
		/// Checks an object if it us a numerical type falling in range of a Ruby Float
		/// </summary>
		/// <param name="value">Object to check</param>
		/// <returns>Flag if object is Float or not</returns>
		private static bool IsRubyFloat(object value)
		{
			if (value is float) return true;
			if (value is double) return true;
			return value is decimal;
		}

		#endregion

		#region Mapping

		/// <summary>
		/// Checks if object is already mapped using equality comparison, mapping object if not found
		/// </summary>
		/// <param name="data">Reference to a list of objects</param>
		/// <param name="obj">Object to map</param>
		/// <returns>Flag if object was mapped</returns>
		/// <remarks>If object is already mapped, the index it was found in is dumped instead of the
		/// the whole object</remarks>
		private static bool TryMapEquality(ref List<dynamic> data, dynamic obj) 
		{
			int index = -1;
			for (int i = 0; i < data.Count; i++)
			{
				if (data[i] == obj)
				{
					index = i;
					break;
				}
			}
			if (index < 0)
			{
				DumpInt32(data.Count);
				data.Add(obj);
				return true;
			}
			DumpInt32(index);
			return false;
		}

		/// <summary>
		/// Checks if object is already mapped using identity comparison, mapping object if not found
		/// </summary>
		/// <param name="data">Reference to a list of objects</param>
		/// <param name="obj">Object to map</param>
		/// <returns>Flag if object was mapped</returns>
		/// <remarks>If object is already mapped, the index it was found in is dumped instead of the
		/// the whole object</remarks>
		private static bool TryMapIdentity(ref List<dynamic> data, dynamic obj) 
		{
			int index = data.IndexOf(obj);
			if (index < 0)
			{
				DumpInt32(data.Count);
				data.Add(obj);
				return true;
			}
			DumpInt32(index);
			return false;
		}

		/// <summary>
		/// Retrieves a <see cref="System.Type"/> that was previously mapped, or if not found, 
		/// finds the type and maps it.
		/// </summary>
		/// <param name="classPath">Path of the class</param>
		/// <returns>Object type</returns>
		/// <exception cref="TypeLoadException">Thrown when type cannot be found in the assembly</exception>
		private static Type GetMappedType(string classPath)
		{
			if (_mappedTypes.ContainsKey(classPath))
				return _mappedTypes[classPath];


			string[] nameArray = Regex.Split(classPath, "::");
			foreach (string typeName in _assemblyTypes.Keys)
			{
				string[] typeArray = Regex.Split(typeName, @"[\+|\.]");
				if (typeArray.SequenceEqual(nameArray))
				{
					_mappedTypes[classPath] = _assemblyTypes[typeName];
					return _mappedTypes[classPath];
				}
			}


			/*
			var regex = new Regex(String.Join(@"[\+|\.]", Regex.Split(classPath, "::")));
			foreach (string typeName in _assemblyTypes.Keys.Where(typeName => regex.Match(typeName).Success))
			{
			    _mappedTypes[classPath] = _assemblyTypes[typeName];
			    return _mappedTypes[classPath];
			}
			*/
			throw new TypeLoadException(String.Format("Type of \"{0}\" cannot be found in loaded assemblies.", classPath));
		}

		/// <summary>
		/// Retrieves the object with the given ID in the map, or null if not found
		/// </summary>
		/// <param name="list">Reference to the map to search</param>
		/// <param name="id">ID of the object</param>
		/// <returns>Dynamic object found with the given ID, or null if not found</returns>
		private static dynamic FindMapping(ref List<dynamic> list, int id)
		{
            return id < list.Count ? list[id] : null;
		}

		/// <summary>
		/// Maps an object to the given list
		/// </summary>
		/// <param name="list">Reference to the map</param>
		/// <param name="obj">Object to map</param>
		private static void MapObject(ref List<dynamic> list, dynamic obj)
		{
			list.Add(obj);
		}

		#endregion

		#region Int32

		/// <summary>
		/// Converts an Int32 to a four-byte, little-endian array and writes it to the stream
		/// </summary>
		/// <param name="int32">Integer to dump</param>
		private static void DumpInt32(int int32)
		{
			byte[] bytes = BitConverter.GetBytes(int32);
			if (!BitConverter.IsLittleEndian)
				Array.Reverse(bytes);
			_stream.Write(bytes, 0, 4);
		}

		/// <summary>
		/// Loads a <see cref="Int32"/> from the stream
		/// </summary>
		/// <returns>Integer value</returns>
		private static int LoadInt32()
		{
			return BitConverter.ToInt32(_stream.ReadBytes(4), 0);
		}

		#endregion

		#region NilClass

		/// <summary>
		/// Writes a null-type marker to the stream.
		/// </summary>
		private static void DumpNilClass()
		{
			_stream.WriteByte((byte)RubyTypes.NilClass);
		}

		/// <summary>
        /// Returns <see langword="null"/>.
		/// </summary>
		/// <returns>null</returns>
		private static object LoadNilClass() { return null; }

		#endregion

		#region FalseClass

		/// <summary>
		/// Writes <see cref="Boolean"/> to the stream.
		/// </summary>
		private static void DumpFalseClass()
		{
			_stream.WriteByte((byte)RubyTypes.FalseClass);
		}

		/// <summary>
		/// Returns <see langword="false"/>.
		/// </summary>
		/// <returns>false</returns>
		private static bool LoadFalseClass() { return false; }

		#endregion

		#region TrueClass

		/// <summary>
        /// Writes <see cref="Boolean"/> to the stream.
		/// </summary>
		private static void DumpTrueClass()
		{
			_stream.WriteByte((byte)RubyTypes.TrueClass);
		}

		/// <summary>
        /// Returns <see langword="true"/>.
		/// </summary>
		/// <returns>true</returns>
		private static bool LoadTrueClass() { return true; }

		#endregion

		#region Fixnum

		/// <summary>
		/// Writes an object to the string as a Ruby Fixnum (<see cref="Int32"/>).
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void DumpFixnum(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.Fixnum);
			DumpInt32((int)obj);
		}

		/// <summary>
		/// Reads a <see cref="Int32"/> from the stream
		/// </summary>
		/// <returns>Integer value</returns>
		private static int LoadFixnum() { return LoadInt32(); }

		#endregion

		#region Bignum

		/// <summary>
        /// Writes an object to the string as a Ruby Bignum (<see cref="Int32"/>).
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void DumpBignum(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.Bignum);
			DumpInt32((int)obj);
		}

		/// <summary>
        /// Reads a <see cref="Int32"/> from the stream
		/// </summary>
		/// <returns>Integer value</returns>
		private static int LoadBignum() { return LoadInt32(); }

		#endregion

		#region Float

		/// <summary>
		/// Writes a <see cref="Single"/> to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void DumpFloat(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.Float);
			byte[] bytes = BitConverter.GetBytes((float)obj);
			if (!BitConverter.IsLittleEndian)
				Array.Reverse(bytes);
			_stream.Write(bytes, 0, 4);
		}

		/// <summary>
		/// Reads a <see cref="Single"/> from the stream
		/// </summary>
		/// <returns>Float value</returns>
		private static float LoadFloat()
		{
			return BitConverter.ToSingle(_stream.ReadBytes(4), 0);
		}

		#endregion

		#region String

		/// <summary>
		/// Writes a <see cref="String"/> to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
        /// <remarks>Strings are serialized in UTF-8 encoding (<see cref="System.Text.Encoding.UTF8"/>).</remarks>
		private static void DumpString(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.String);
			if (!TryMapEquality(ref _strings, obj))
				return;
			string data = Convert.ToString(obj);
			DumpInt32(data.Length);				// Dump length
			byte[] bytes = data.GetBytes();         // Get UTF-8 formatted string as byte array
			_stream.Write(bytes, 0, bytes.Length);  // Dump bytes
		}

		/// <summary>
		/// Reads a <see cref="String"/> from the stream
		/// </summary>
		/// <returns>String value</returns>
        /// <remarks>Strings are returned in UTF-8 encoding (<see cref="System.Text.Encoding.UTF8"/>).</remarks>
		private static string LoadString()
		{
			int id = LoadInt32();
			string obj = FindMapping(ref _strings, id);
			if (obj != null)
				return String.Copy(obj);
			int size = LoadInt32();
			obj = _stream.ReadByteString(size);
			MapObject(ref _strings, obj);
			return obj;
		}

		#endregion

		#region Array

		/// <summary>
		/// Writes an <see cref="Array"/> to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void DumpArray(dynamic obj)
		{
			_stream.WriteByte((byte)RubyTypes.Array);
            if (TryMapIdentity(ref _arrays, obj))
            {
                DumpInt32(obj.Count);
                foreach (dynamic data in obj)
                    ArcDump(data);
            }
		}

		/// <summary>
		/// Reads an <see cref="Array"/> from the stream
		/// </summary>
		/// <returns>Array value</returns>
		/// <remarks>All returned values that are of "Array" type are returned as 
		/// a <see cref="List{dynamic}"/>.</remarks>
		private static List<dynamic> LoadArray()
		{
			int id = LoadInt32();
			List<dynamic> obj = FindMapping(ref _arrays, id);
            if (obj != null)
                return obj;
			int size = LoadInt32();
			obj = new List<dynamic>(size);
			for (int i = 0; i < size; i++)
				obj.Add(ArcLoad());
			MapObject(ref _arrays, obj);
			return obj;
		}

		#endregion

		#region Hash

		/// <summary>
		/// Writes a dictionary-type to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void DumpHash(dynamic obj)
		{
			_stream.WriteByte((byte)RubyTypes.Hash);
            if (TryMapIdentity(ref _hashes, obj))
            {
                DumpInt32(obj.Count);
                foreach (var kvPair in obj)
                {
                    ArcDump(kvPair.Key);
                    ArcDump(kvPair.Value);
                }
            }
		}

		/// <summary>
        /// Reads a <see cref="Hash"/> type from the stream.
		/// </summary>
		/// <returns>Hash value</returns>
		private static Hash LoadHash()
		{
			int id = LoadInt32();
			Hash obj = FindMapping(ref _hashes, id);
			if (obj != null)
				return obj;
			int size = LoadInt32();
			obj = new Hash();
			object key;
			for (int i = 0; i < size; i++)
			{
				key = ArcLoad();
				obj[key] = ArcLoad();
			}
			MapObject(ref _hashes, obj);
			return obj;
		}

		#endregion

		#region Object

		/// <summary>
		/// Writes an <see cref="Object"/> to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void DumpObject(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.Object);
			Type objType = obj.GetType();
			string classe = Regex.Replace(objType.ToString(), @"[\+|\.]", "::");
			DumpString(classe);
			if (!TryMapIdentity(ref _objects, obj))
				return;
			if (obj.HasMethod("_arc_dump"))
			{
				var data = (byte[])objType.InvokeMember(
					"_arc_dump",
					BindingFlags.Public | BindingFlags.InvokeMethod,
					null,
					obj,
					null
				);
				DumpInt32(data.Length);
				_stream.Write(data, 0, data.Length);
			}
			else
			{
				var excludes = new List<dynamic>();
				if (obj.HasMethod("_arc_exclude"))
				{
					excludes = (List<dynamic>)objType.InvokeMember(
						"_arc_exclude",
						BindingFlags.Public | BindingFlags.GetProperty,
						null,
						obj,
						null
					);
				}
				PropertyInfo[] properties =
					objType.GetProperties(BindingFlags.Public | BindingFlags.Instance);
				var variables = properties.Select(info => info.Name).Where(variable => 
                    !excludes.Contains(variable)).ToList();
			    variables.Sort();
				DumpInt32(variables.Count);
				foreach (var variable in variables)
				{
					DumpString(variable);
					var value = objType.InvokeMember(
						variable,
						BindingFlags.Public | BindingFlags.GetProperty | BindingFlags.Instance,
						null,
						obj,
						null
					);
					ArcDump(value);
				}
			}
		}

		/// <summary>
		/// Loads an <see cref="Object"/> from the stream.
		/// </summary>
		/// <returns>Deserialized object.</returns>
		private static dynamic LoadObject()
		{
			string mapString = ArcLoad();
			int id = LoadInt32();
			dynamic obj = FindMapping(ref _objects, id);
			if (obj != null)
				return obj;
            Type type = GetMappedType(mapString);
			int size = LoadInt32();
			if (type.GetMethod("_arc_load") != null)
			{
				obj = type.InvokeMember(
					"_arc_load", BindingFlags.Public | BindingFlags.Static | BindingFlags.InvokeMethod,
					null, type, new object[] { _stream.ReadBytes(size) });
                MapObject(ref _objects, obj);
				return obj;
			}
			obj = Activator.CreateInstance(type);
			string propertyName;
			dynamic propertyValue;
			for (int i = 0; i < size; i++)
			{
				propertyName = ArcLoad();		
				propertyValue = ArcLoad();
				PropertyInfo info = type.GetProperty(propertyName);
				if (info != null)
					info.SetValue(obj, propertyValue, null);
			}
			MapObject(ref _objects, obj);
			return obj;
		}

		#endregion
	}
}
