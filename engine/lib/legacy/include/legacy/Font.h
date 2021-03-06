#ifndef LEGACY_FONT_H
#define LEGACY_FONT_H

#include <ruby.h>

#include <hltypes/harray.h>
#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>

#include "legacyExport.h"
#include "RubyObject.h"

namespace legacy
{
	class Color;

	extern VALUE rb_cFont;

	/// @brief Emulates RGSS's Font class.
	class legacyExport Font : public RubyObject
	{
	public:
		/// @brief Constructor.
		Font();
		/// @brief Constructor.
		/// @param[in] name Font name.
		Font(chstr name);
		/// @brief Constructor.
		/// @param[in] name Font name.
		/// @param[in] size Font size.
		Font(chstr name, int size);
		/// @brief Destructor.
		~Font();
		/// @brief Initializes the basic object.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		void initialize(int argc, VALUE* argv);
		/// @brief Ruby garbage collector marking.
		void mark();

		HL_DEFINE_GET(hstr, name, Name);
		HL_DEFINE_GET(int, size, Size);
		HL_DEFINE_GET(bool, bold, Bold);
		HL_DEFINE_GET(bool, italic, Italic);
		HL_DEFINE_GET(Color*, color, Color);
		/// @brief Gets the Atres font name.
		/// @return Atres font name.
		hstr getAtresFontName();

		/// @brief Generates a Font defintion for the current render if necessary.
		/// @param[in] font The font instance.
		static void generate(Font* font);

		/// @brief Default Font name.
		static hstr defaultName;
		/// @brief Default Font size.
		static int defaultSize;
		/// @brief Default Bold flag.
		static bool defaultBold;
		/// @brief Default Italic flag.
		static bool defaultItalic;
		/// @brief Default Font Color.
		static Color* defaultColor;
		/// @brief Default Font Color.
		static VALUE rb_defaultColor;

		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Sets the font parameters.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Used for clone and dup.
		/// @param[in] original The original.
		static VALUE rb_initialize_copy(VALUE self, VALUE original);
		/// @brief Creates a C++ version of this class.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		static VALUE create(int argc, VALUE* argv);

		/// @brief Gets the font's name.
		/// @return Name of the font.
		static VALUE rb_getName(VALUE self);
		/// @brief Sets the font's name.
		/// @param[in] value Name of the font.
		static VALUE rb_setName(VALUE self, VALUE value);
		/// @brief Gets the font's size.
		/// @return Value of the font's size.
		static VALUE rb_getSize(VALUE self);
		/// @brief Sets the font's size.
		/// @param[in] value Value of the font's size.
		static VALUE rb_setSize(VALUE self, VALUE value);
		/// @brief Gets the font's bold value.
		/// @return bool Value of bold parameter.
		static VALUE rb_getBold(VALUE self);
		/// @brief Sets the font's bold value.
		/// @param[in] bool Value of bold parameter.
		static VALUE rb_setBold(VALUE self, VALUE value);
		/// @brief Gets the font's italic value.
		/// @return bool Value of italic parameter.
		static VALUE rb_getItalic(VALUE self);
		/// @brief Sets the font's italic value.
		/// @param[in] bool Value of italic parameter.
		static VALUE rb_setItalic(VALUE self, VALUE value);
		/// @brief Gets the font's color.
		/// @return The Color value used for the font.
		static VALUE rb_getColor(VALUE self);
		/// @brief Sets the font's color.
		/// @param[in] value The Color used for the font.
		static VALUE rb_setColor(VALUE self, VALUE value);

		/// @brief Gets the font's name.
		/// @return Default name of the font.
		static VALUE rb_getDefaultName(VALUE classe);
		/// @brief Sets the font's name.
		/// @param[in] value Default name of the font.
		static VALUE rb_setDefaultName(VALUE classe, VALUE value);
		/// @brief Gets the font's size.
		/// @return Default value of the font's size.
		static VALUE rb_getDefaultSize(VALUE classe);
		/// @brief Sets the font's size.
		/// @param[in] value Default value of the font's size.
		static VALUE rb_setDefaultSize(VALUE classe, VALUE value);
		/// @brief Gets the font's bold value.
		/// @return Default value of bold parameter.
		static VALUE rb_getDefaultBold(VALUE classe);
		/// @brief Sets the font's bold value.
		/// @param[in] value Default value of bold parameter.
		static VALUE rb_setDefaultBold(VALUE classe, VALUE value);
		/// @brief Gets the font's italic value.
		/// @return bool Default value of italic parameter.
		static VALUE rb_getDefaultItalic(VALUE classe);
		/// @brief Sets the font's italic value.
		/// @param[in] value Default value of italic parameter.
		static VALUE rb_setDefaultItalic(VALUE classe, VALUE value);
		/// @brief Gets the font's color.
		/// @return Default Color used for the font.
		static VALUE rb_getDefaultColor(VALUE classe);
		/// @brief Sets the font's color.
		/// @param[in] value Default Color used for the font.
		static VALUE rb_setDefaultColor(VALUE classe, VALUE value);

		/// @brief Mimics a dumping method to prevent dumping of this class.
		static VALUE rb_arcDump(VALUE self);

	protected:
		/// @brief Font name.
		hstr name;
		/// @brief Font size.
		int size;
		/// @brief Bold flag.
		bool bold;
		/// @brief Italic flag.
		bool italic;
		/// @brief Font Color.
		Color* color;
		/// @brief Ruby object of font Color.
		VALUE rb_color;

		/// @brief Gets the name for Atres TTF.
		/// @return The name for Atres TTF.
		hstr _getAtresTtfName();

		/// @brief Keeps track of missing fonts so they aren't checked multiple times.
		static harray<hstr> _missingFonts;

	};

}
#endif
