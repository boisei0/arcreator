#region Using Directives

using System;
using System.ComponentModel;

#endregion


namespace ARCed.Scintilla
{
    public abstract class ScintillaHelperBase : IDisposable
    {
        #region Fields

        private bool _isDisposed;
        private INativeScintilla _nativeScintilla;
        private Scintilla _scintilla;

        #endregion Fields


        #region Methods

        private void scintilla_Load(object sender, EventArgs e)
        {
            this.Initialize();
        }


        public virtual void Dispose()
        {
            this._isDisposed = true;
        }


        //	[workitem:24911] 2000-10-04 Chris Rickard
        //	This was put in specifically for Markers but it actually makes a lot of sense for all
        //	ScintillaHelpers. 
        //	Original Code by fxa. I changed the implementation slightly so that I can make Equals
        //	abstract, forcing all Helpers to implement their own.
        /// <summary>
        ///     Abstract Equals Override. All Helpers must implement this. Use IsSameHelperFamily to
        ///     determine if the types are compatible and they have the same Scintilla. For most top 
        ///     level helpers like Caret and Lexing this should be enough. Helpers like Marker and
        ///     Line also need to take other variables into consideration.
        /// </summary>
        /// <param name="obj"></param>
        /// <returns></returns>
        public abstract override bool Equals(object obj);


        //	Supress warning
        public override int GetHashCode()
        {
            return base.GetHashCode();
        }


        protected internal virtual void Initialize(){}


        /// <summary>
        ///     Determines if obj belongs to the same Scintilla and is of compatible type
        /// </summary>
        protected bool IsSameHelperFamily(object obj)
        {
            var other = obj as ScintillaHelperBase;
            if (other == null)
                return false;

            if (this._scintilla == null || other._scintilla == null)
                return false;

             if(!this._scintilla.Equals(other._scintilla))
                 return false;

             return GetType().IsAssignableFrom(obj.GetType());
        }

        #endregion Methods


        #region Properties

        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public bool IsDisposed
        {
            get
            {
                return this._isDisposed;
            }
            set
            {
                this._isDisposed = value;
            }
        }


        protected internal INativeScintilla NativeScintilla
        {
            get { return this._nativeScintilla; }
        }


        public Scintilla Scintilla
        {
            get { return this._scintilla; }
            set 
            { 
                this._scintilla = value;
                this._nativeScintilla = this._scintilla;
            }
        }

        #endregion Properties


        #region Constructors

        protected internal ScintillaHelperBase(Scintilla scintilla)
        {
            this._scintilla = scintilla;
            this._nativeScintilla = scintilla;
        }

        #endregion Constructors
    }
}
