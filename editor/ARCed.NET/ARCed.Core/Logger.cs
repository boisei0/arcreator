﻿#region Using Directives

using System;
using System.IO;
using System.Text;

#endregion

namespace ARCed.Core
{
	/// <summary>
	/// Events arguments used when a text is added to a Logger
	/// </summary>
	public class LogTextEventArgs : EventArgs
	{
		/// <summary>
		/// The text added to the Logger
		/// </summary>
		public string AddedText { get; private set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		/// <param name="text">Text added to the Logger</param>
		public LogTextEventArgs(string text)
		{
			this.AddedText = text;
		}
	}

	/// <summary>
	/// Events arguments used when a Logger is saved
	/// </summary>
	public class LogSaveEventArgs : EventArgs
	{
		/// <summary>
		/// FullPath where the file is saved
		/// </summary>
		public string Filename { get; private set; }
		/// <summary>
		/// Flag is save was successful
		/// </summary>
		public bool Successful { get; private set; }
		/// <summary>
		/// Flag is buffer was cleared
		/// </summary>
		public bool BufferCleared { get; private set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		/// <param name="filename">FullPath where the file is saved</param>
		/// <param name="success">Flag is save was successful</param>
		/// <param name="flushed">Flag is buffer was cleared</param>
		public LogSaveEventArgs(string filename, bool success, bool flushed)
		{
			this.Filename = filename;
			this.Successful = success;
			this.BufferCleared = flushed;
		}
	}

	/// <summary>
	/// Class for creating a buffer and adding text to. Acts as a loose wrapper for 
	/// a StringBuilder object, but includes events raised when text is added or when
	/// the buffer is flushed to a file.
	/// </summary>
	public class Logger
	{
		private readonly StringBuilder _buffer;
		private static string _header;

		/// <summary>
		/// Delegate handler for the OnSave event
		/// </summary>
		/// <param name="sender">Invoker of the even</param>
		/// <param name="e">Event arguments</param>
		public delegate void OnSaveHandler(object sender, LogSaveEventArgs e);
		/// <summary>
		/// Event raised when the Logger is saved to disk
		/// </summary>
		public event OnSaveHandler OnSave;
		/// <summary>
		/// Delegate handler for the NoteTextChanged event
		/// </summary>
		/// <param name="sender">Invoker of the even</param>
		/// <param name="e">Event arguments</param>
		public delegate void TextChangedHandler(object sender, LogTextEventArgs e);
		/// <summary>
		/// Event raised when text is added to the Logger
		/// </summary>
		public event TextChangedHandler TextChanged;

		/// <summary>
		/// Gets or sets the text of the Logger
		/// </summary>
		public string Text
		{
			get { return this._buffer.ToString(); }
			set
			{
				this._buffer.Clear();
				this._buffer.Append(value);
				if (this.TextChanged != null)
					this.TextChanged(this, new LogTextEventArgs(value));
			}
		}

		/// <summary>
		/// Gets the buffer
		/// </summary>
		public StringBuilder Buffer { get { return this._buffer; } }

		/// <summary>
		/// Default contructor
		/// </summary>
		public Logger()
		{
			this._buffer = new StringBuilder();
			_header = "------------------------------------------------\n";
		}

		/// <summary>
		/// Saves the log file to disk
		/// </summary>
		/// <param name="filename">FullPath where log is saved</param>
		/// <param name="flushBuffer">Flag to clear the buffer after saving</param>
		public void Save(string filename, bool flushBuffer)
		{
			bool result;
			try
			{
				File.WriteAllText(filename, this._buffer.ToString(), Encoding.UTF8);
				if (flushBuffer)
					this._buffer.Clear();
				result = true;
			}
			catch { result = false; }
			if (this.OnSave != null)
				this.OnSave(this, new LogSaveEventArgs(filename, result, flushBuffer));
		}

		/// <summary>
		/// Appends a header to the log file to denote a new section
		/// </summary>
		/// <param name="message">The text within the header</param>
		public void AppendHeader(string message)
		{
			this._buffer.AppendLine(_header);
			this._buffer.AppendLine(message);
			this._buffer.AppendLine(_header);
			if (this.TextChanged != null)
			{
				var args = new LogTextEventArgs(_header);
				this.TextChanged(this, args);
				this.TextChanged(this, new LogTextEventArgs(message + "\n"));
				this.TextChanged(this, args);
			}
		}

		/// <summary>
		/// Clears the buffer of all logged text
		/// </summary>
		/// <param name="notify">Flag to fire NoteTextChanged event</param>
		public void Clear(bool notify = false)
		{
			this._buffer.Clear();
			if (notify && this.TextChanged != null)
				this.TextChanged(this, new LogTextEventArgs(""));
		}

		/// <summary>
		/// Appends the text to the log
		/// </summary>
		/// <param name="text">Text to append</param>
		public void Append(string text)
		{
			this._buffer.Append(text);
			if (this.TextChanged != null)
				this.TextChanged(this, new LogTextEventArgs(text));
			LogConsole(text);
		}

		/// <summary>
		/// Appends the string representation of the object to the log
		/// </summary>
		/// <param name="obj">Object to append</param>
		public void Append(object obj)
		{
			this._buffer.Append(obj);
			if (this.TextChanged != null)
				this.TextChanged(this, new LogTextEventArgs(obj.ToString()));
			LogConsole(obj);
		}

		/// <summary>
		/// Appends the text to the log and adds a newline
		/// </summary>
		/// <param name="text">Text to append</param>
		public void AppendLine(string text)
		{
			this._buffer.AppendLine(text);
			if (this.TextChanged != null)
				this.TextChanged(this, new LogTextEventArgs(text + "\n"));
			LogConsoleLine(text);
		}

		/// <summary>
		/// Appends the string representation of the object to the log and adds a newline
		/// </summary>
		/// <param name="obj">Object to append</param>
		public void AppendLine(object obj)
		{
			this._buffer.AppendLine(obj.ToString());
			if (this.TextChanged != null)
				this.TextChanged(this, new LogTextEventArgs(obj + "\n"));
			LogConsoleLine(obj);
		}

		/// <summary>
		/// Appends text, replacing items in formatted string with objects
		/// </summary>
		/// <param name="text">Format string</param>
		/// <param name="objs">Object replacements</param>
		public void AppendFormat(string text, params object[] objs)
		{
			string str = String.Format(text, objs);
			this._buffer.Append(str);
			if (this.TextChanged != null)
				this.TextChanged(this, new LogTextEventArgs(str));
			LogConsole(str);
		}

		private static void LogConsole(object obj)
		{
			
			Console.Write(obj);
		}

		private static void LogConsoleLine(object obj)
		{
			Console.WriteLine(obj);
		}
	}
}
