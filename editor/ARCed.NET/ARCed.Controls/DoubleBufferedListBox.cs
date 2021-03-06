﻿#region Using Directives

using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// ListBox control with double-buffering
	/// </summary>
	[ToolboxBitmap(typeof(ListBox))]
	[Description("ListBox control with double-buffering.")]
	public partial class DoubleBufferedListBox : ListBox
	{
		public DoubleBufferedListBox() {
			DoubleBuffered = true;
		}
	}
}
