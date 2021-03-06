﻿namespace RPG
{
    /// <summary>
    /// Data class for map information.
    /// </summary>
	public class MapInfo
	{
        /// <summary>
        /// The map name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// The parent map ID.
        /// </summary>
		public int parent_id { get; set; }
        /// <summary>
        /// The map tree display order, used internally.
        /// </summary>
		public int order { get; set; }
        /// <summary>
        /// The map tree expansion flag, used internally.
        /// </summary>
		public bool expanded { get; set; }
        /// <summary>
        /// The X-axis scroll position, used internally.
        /// </summary>
		public int scroll_x { get; set; }
        /// <summary>
        /// The Y-axis scroll position, used internally.
        /// </summary>
		public int scroll_y { get; set; }
		
        /// <summary>
        /// Creates a new instance of an RPG.MapInfo.
        /// </summary>
		public MapInfo()
		{
			this.name = "";
			this.parent_id = 0;
			this.order = 0;
			this.expanded = false;
			this.scroll_x = 0;
			this.scroll_y = 0;
		}
	}
}
