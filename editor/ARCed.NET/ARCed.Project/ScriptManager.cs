﻿#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Windows.Forms;

#endregion

namespace ARCed.Scripting
{
	/// <summary>
    /// Class used for managing <see cref="ARCed.Scripting.Script"/> objects. The functionality
	/// is a very loose wrapper for a list.
	/// </summary>
	public class ScriptManager
	{
		private static List<Script> _scripts;

		/// <summary>
		/// Gets a list of all loaded scripts
		/// </summary>
		public List<Script> Scripts
		{
			get { return _scripts; }
		}

		/// <summary>
		/// Returns a new instance of the ScriptManager
		/// </summary>
		/// <param name="parentDirectory">The parent directory of the scripts</param>
		public ScriptManager(string parentDirectory)
		{
			_scripts = new List<Script>();
			this.LoadScripts(parentDirectory);
		}

		/// <summary>
		/// Loads scripts from the default directory
		/// </summary>
		public void LoadScripts() { this.LoadScripts(Project.ScriptsDirectory); }

		/// <summary>
		/// Loads scripts from the given directory
		/// </summary>
		/// <param name="directory"></param>
		public void LoadScripts(string directory)
		{
			_scripts.Clear();
			foreach (string file in Directory.GetFiles(directory, "*.rb"))
				_scripts.Add(new Script(file));
			this.RefreshScriptIndices();
		}

		/// <summary>
		/// Adds a script into the manager
		/// </summary>
		/// <param name="script">The script to add</param>
		public void Add(Script script)
		{
			this.Scripts.Add(script);
			this.RefreshScriptIndices();
		}

		/// <summary>
		/// Adds a script into the manager
		/// </summary>
		/// <param name="filename">The path of the script</param>
		/// <remarks>Only files with an ".rb" extension will be added</remarks>
		public void Add(string filename)
		{
			if (Path.GetExtension(filename) == ".rb")
			{
				this.Scripts.Add(new Script(filename));
				this.RefreshScriptIndices();
			}
		}

		/// <summary>
		/// Creates and adds multiple scripts into the manager
		/// </summary>
		/// <param name="scripts">An array of scripts</param>
		public void AddRange(IEnumerable<Script> scripts)
		{
			foreach (Script script in scripts)
				this.Scripts.Add(script);
			this.RefreshScriptIndices();
		}

		/// <summary>
		/// Creates and adds multiple scripts into the manager
		/// </summary>
		/// <param name="filenames">The filenames of the scripts</param>
		/// <remarks>Only files with an ".rb" extension will be added</remarks>
		public void AddRange(IEnumerable<string> filenames)
		{
			foreach (string filename in filenames)
			{
				if (Path.GetExtension(filename) == ".rb")
					this.Scripts.Add(new Script(filename));
			}
			this.RefreshScriptIndices();
		}

		/// <summary>
		/// Inserts a script at the given index
		/// </summary>
		/// <param name="script">The script to insert</param>
		/// <param name="index">The index where it will be inserted</param>
		public void Insert(Script script, int index)
		{
			this.Scripts.Insert(index, script);
			this.RefreshScriptIndices();
		}

		/// <summary>
		/// Removes the script from the manager
		/// </summary>
		/// <param name="script">The script to remove</param>
		public void Remove(Script script)
		{
			this.Scripts.Remove(script);
			this.RefreshScriptIndices();
		}

		/// <summary>
		/// Removes the script at the given index
		/// </summary>
		/// <param name="index">The index of the script</param>
		public void Remove(int index)
		{
			this.Scripts.RemoveAt(index);
			this.RefreshScriptIndices();
		}

		/// <summary>
		/// Saves the script at the given index
		/// </summary>
		/// <param name="index">The index of the script</param>
		/// <returns>Truth value of successful save</returns>
		public bool Save(int index)
		{
			return this.Scripts[index].Save();
		}

		/// <summary>
		/// Applies changes and saves all scripts to disk
		/// </summary>
		public void SaveAll()
		{
			var errors = new List<string>();
			for (int i = 0; i < this.Scripts.Count; i++)
			{
				this.Scripts[i].Index = i;
				if (!this.Scripts[i].Save())
					errors.Add(this.Scripts[i].Title);
			}
			if (errors.Count > 0)
			{
				string msg = String.Format("Failed to save the following script(s):\n{0}",
					String.Join("\n\t", errors));
				MessageBox.Show(msg, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
			}
		}

		/// <summary>
		/// Returns a binding list to be used with form controls
		/// </summary>
		public BindingList<Script> BindingList
		{
			get
			{
				var binding = new BindingList<Script>(this.Scripts)
				{
				    AllowNew = true
				};
			    return binding;
			}
			set { _scripts = value.ToList(); }
		}

		/// <summary>
		/// Refreshes the indices of all loaded scripts to match their current position in the list
		/// </summary>
		public void RefreshScriptIndices()
		{
			for (int i = 0; i < this.Scripts.Count; i++)
				this.Scripts[i].Index = i;
		}

		/// <summary>
		/// Finds a and returns the script with the given filename.
		/// </summary>
		/// <param name="path">The path to script to be found</param>
		/// <returns>The path to the script if found, null otherwise</returns>
		public Script WithPath(string path)
		{
			return _scripts.Find(s => s.Filename == path);
		}
	}
}
