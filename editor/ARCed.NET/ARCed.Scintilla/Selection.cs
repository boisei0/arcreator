#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class Selection : TopLevelHelper
    {
        #region Fields

        private Color _backColorUnfocused = Color.LightGray;
        private bool _hidden;
        private bool _hideSelection;

        #endregion Fields


        #region Methods

        public void Clear()
        {
            NativeScintilla.Clear();
        }


        private void ResetBackColor()
        {
            this.BackColor = SystemColors.Highlight;
        }


        private void ResetBackColorUnfocused()
        {
            this.BackColorUnfocused = Color.LightGray;
        }


        private void ResetEnd()
        {
            this.End = 0;
        }


        private void ResetForeColor()
        {
            this.ForeColor = SystemColors.HighlightText;
        }


        private void ResetForeColorUnfocused()
        {
            this.ForeColorUnfocused = SystemColors.HighlightText;
        }


        private void ResetHidden()
        {
            this.Hidden = false;
        }


        private void ResetHideSelection()
        {
            this._hideSelection = false;
        }


        private void ResetMode()
        {
            this.Mode = SelectionMode.Stream;
        }


        private void ResetStart()
        {
            this.Start = 0;
        }


        public void SelectAll()
        {
            NativeScintilla.SelectAll();
        }


        public void SelectNone()
        {
            NativeScintilla.SetSel(-1, -1);
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeBackColor() | 
                this.ShouldSerializeBackColorUnfocused() | 
                this.ShouldSerializeForeColor() | 
                this.ShouldSerializeForeColorUnfocused() | 
                this.ShouldSerializeHidden() |
                this.ShouldSerializeHideSelection() |
                this.ShouldSerializeMode();
        }


        private bool ShouldSerializeBackColor()
        {
            return this.BackColor != SystemColors.Highlight;
        }


        private bool ShouldSerializeBackColorUnfocused()
        {
            return this.BackColorUnfocused != Color.LightGray;
        }


        private bool ShouldSerializeEnd()
        {
            return this.End != 0;
        }


        private bool ShouldSerializeForeColor()
        {
            return this.ForeColor != SystemColors.HighlightText;
        }


        private bool ShouldSerializeForeColorUnfocused()
        {
            return this.ForeColorUnfocused != SystemColors.HighlightText;
        }


        private bool ShouldSerializeHidden()
        {
            return this._hidden;
        }


        private bool ShouldSerializeHideSelection()
        {
            return this._hideSelection;
        }


        private bool ShouldSerializeMode()
        {
            return this.Mode != SelectionMode.Stream;
        }


        private bool ShouldSerializeStart()
        {
            return this.Start != 0;
        }

        #endregion Methods


        #region Properties

        public Color BackColor
        {
            get
            {
                if (Scintilla.ColorBag.ContainsKey("Selection.BackColor"))
                    return Scintilla.ColorBag["Selection.BackColor"];

                return SystemColors.Highlight;
            }
            set
            {
                if (value == this.BackColor)
                    return;

                if (value == SystemColors.Highlight)
                    Scintilla.ColorBag.Remove("Selection.BackColor");
                else
                    Scintilla.ColorBag["Selection.BackColor"] = value;

                if (Scintilla.ContainsFocus)
                    NativeScintilla.SetSelBack(value != Color.Transparent, Utilities.ColorToRgb(value));
            }
        }


        public Color BackColorUnfocused
        {
            get
            {
                if (Scintilla.ColorBag.ContainsKey("Selection.BackColorUnfocused"))
                    return Scintilla.ColorBag["Selection.BackColorUnfocused"];

                return Color.LightGray;
            }
            set
            {
                if (value == this.BackColorUnfocused)
                    return;

                if (value == Color.LightGray)
                    Scintilla.ColorBag.Remove("Selection.BackColorUnfocused");
                else
                    Scintilla.ColorBag["Selection.BackColorUnfocused"] = value;
                
                if(!Scintilla.ContainsFocus)
                    NativeScintilla.SetSelBack(value != Color.Transparent, Utilities.ColorToRgb(value));
            }
        }


        public int End
        {
            get
            {
                return NativeScintilla.GetSelectionEnd();
            }
            set
            {
                NativeScintilla.SetSelectionEnd(value);
            }
        }


        public Color ForeColor
        {
            get
            {
                if (Scintilla.ColorBag.ContainsKey("Selection.ForeColor"))
                    return Scintilla.ColorBag["Selection.ForeColor"];

                return SystemColors.HighlightText;
            }
            set
            {
                if (value == SystemColors.HighlightText)
                    Scintilla.ColorBag.Remove("Selection.ForeColor");
                else
                    Scintilla.ColorBag["Selection.ForeColor"] = value;
                
                if (Scintilla.ContainsFocus)
                    NativeScintilla.SetSelFore(value != Color.Transparent, Utilities.ColorToRgb(value));
            }
        }


        public Color ForeColorUnfocused
        {
            get
            {
                if (Scintilla.ColorBag.ContainsKey("Selection.ForeColorUnfocused"))
                    return Scintilla.ColorBag["Selection.ForeColorUnfocused"];

                return SystemColors.HighlightText;
            }
            set
            {
                if (value == this.ForeColorUnfocused)
                    return;

                if (value == SystemColors.HighlightText)
                    Scintilla.ColorBag.Remove("Selection.ForeColorUnfocused");
                else
                    Scintilla.ColorBag["Selection.ForeColorUnfocused"] = value;
                
                if(!Scintilla.ContainsFocus)
                    NativeScintilla.SetSelFore(value != Color.Transparent, Utilities.ColorToRgb(value));
            }
        }


        public bool Hidden
        {
            get
            {
                return this._hidden;
            }
            set
            {
                this._hidden = value;
                NativeScintilla.HideSelection(value);
            }
        }


        public bool HideSelection
        {
            get
            {
                return this._hideSelection;
            }
            set
            {
                this._hideSelection = value;
                
                if (!Scintilla.ContainsFocus)
                    NativeScintilla.HideSelection(value);
            }
        }


        [Browsable(false)]
        public bool IsRectangle
        {
            get
            {
                return NativeScintilla.SelectionIsRectangle();
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public int Length
        {
            get
            {
                return Math.Abs(this.End - this.Start);
            }
            set
            {
                //hope this is ok, seemed like an easy feature to add, just these lines, hope it doesn't break anything
                this.End = this.Start + value;
            }
        }


        public SelectionMode Mode
        {
            get
            {
                return (SelectionMode)NativeScintilla.GetSelectionMode();
            }
            set
            {
                NativeScintilla.SetSelectionMode((int)value);
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public Range Range
        {
            get
            {
                return new Range(NativeScintilla.GetSelectionStart(), NativeScintilla.GetSelectionEnd(), Scintilla);
            }
            set
            {
                NativeScintilla.SetSel(value.Start, value.End);
            }
        }


        public int Start
        {
            get
            {
                return NativeScintilla.GetSelectionStart();
            }
            set
            {
                NativeScintilla.SetSelectionStart(value);
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public string Text
        {
            get
            {
                string s;
                NativeScintilla.GetSelText(out s);
                return s;
            }
            set
            {
                if(string.IsNullOrEmpty(value))
                    this.Clear();
                else
                    NativeScintilla.ReplaceSel(value);
            }
        }

        #endregion Properties


        #region Constructors

        protected internal Selection(Scintilla scintilla) : base(scintilla)
        {
            NativeScintilla.SetSelBack(this.BackColor != Color.Transparent, Utilities.ColorToRgb(this.BackColor));
            NativeScintilla.SetSelFore(this.ForeColor != Color.Transparent, Utilities.ColorToRgb(this.ForeColor));
        }

        #endregion Constructors
    }
}
