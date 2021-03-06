﻿#region Using Directives



#endregion Using Directives


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Controls find behavior for non-regular expression searches
    /// </summary>
    public enum FindOption
    {
        /// <summary>
        ///     Find must match the whole word
        /// </summary>
        WholeWord = 2,

        /// <summary>
        ///     Find must match the case of the expression
        /// </summary>
        MatchCase = 4,

        /// <summary>
        ///     Only match the _start of a word
        /// </summary>
        WordStart = 0x00100000,

        /// <summary>
        ///     Not used in ARCed.Scintilla
        /// </summary>
        RegularExpression = 0x00200000,

        /// <summary>
        ///     Not used in ARCed.Scintilla
        /// </summary>
        Posix = 0x00400000,
    }
}
