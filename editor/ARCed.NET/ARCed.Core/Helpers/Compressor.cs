﻿#region Using Directives

using System;
using System.IO;
using System.Windows.Forms;
using SevenZip;

#endregion

namespace ARCed.Helpers
{
    /// <summary>
    /// Static class used for compressing/extracting files and folders using 7zip.
    /// </summary>
	public static class Compressor
	{

		private static SevenZipCompressor _compressor;
		private static SevenZipExtractor _extractor;
		private static bool _notify;

		/// <summary>
		/// Compresses a directory into a single archive
		/// </summary>
		/// <param name="inDir">The path to the directory to compress</param>
		/// <param name="outFile">The archive name to create</param>
		/// <param name="notify">Flag to notify user when finished</param>
		public static void CompressDirectory(string inDir, string outFile, bool notify = false)
		{
			SevenZipBase.SetLibraryPath(PathHelper.SevenZipLibrary);
			if (_compressor == null)
			{
				_compressor = new SevenZipCompressor
				{
				    ArchiveFormat = OutArchiveFormat.SevenZip,
				    CompressionLevel = CompressionLevel.Ultra,
				    CompressionMode = CompressionMode.Create
				};
			}
			_notify = notify;
			_compressor.TempFolderPath = Path.GetTempPath();
			_compressor.CompressDirectory(inDir, outFile);
			File.SetCreationTime(outFile, DateTime.Now);
		}

		/// <summary>
		/// Extracts and archive to the given directory
		/// </summary>
		/// <param name="inFile">Path to the archive to extract</param>
		/// <param name="outDir">The path to the target directory for extraction</param>
		public static void ExtractArchive(string inFile, string outDir)
		{
			SevenZipBase.SetLibraryPath(PathHelper.SevenZipLibrary);
			try
			{
				_extractor = new SevenZipExtractor(inFile);
				if (!Directory.Exists(outDir))
					Directory.CreateDirectory(outDir);
				_extractor.ExtractionFinished += ExtractorExtractionFinished;
				_extractor.BeginExtractArchive(outDir);
			}
			catch
			{
				MessageBox.Show("Failed to extract ARChive.", 
					"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
			}
		}

		private static void ExtractorExtractionFinished(object sender, EventArgs e)
		{
			_extractor.Dispose();
			if (_notify)
				MessageBox.Show("Extraction complete!", "Message");
		}
	}
}
