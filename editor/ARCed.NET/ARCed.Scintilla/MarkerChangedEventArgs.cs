﻿#region Using Directives



#endregion Using Directives


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides data for the MarkerChanged event
    /// </summary>
    public class MarkerChangedEventArgs : ModifiedEventArgs
    {
        #region Fields

        private int _line;

        #endregion Fields


        #region Properties

        /// <summary>
        ///     Returns the line number where the marker change occured
        /// </summary>
        public int Line
        {
            get
            {
                return this._line;
            }
            set
            {
                this._line = value;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the LinesNeedShownEventArgs class.
        /// </summary>
        /// <param name="line">Line number where the marker change occured</param>
        /// <param name="modificationType">What type of Scintilla modification occured</param>
        public MarkerChangedEventArgs(int line, int modificationType) : base(modificationType)
        {
            this._line = line;
        }

        #endregion Constructors
    }
}
