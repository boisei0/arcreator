#include <ruby.h>

#include <april/Window.h>
#include <hltypes/harray.h>
#include <hltypes/hfile.h>
#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

#include "ARC.h"
#include "System.h"

namespace reactor
{
	VALUE rb_mARC;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	hstr ARC::Version;
	
	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void ARC::init()
	{
		Version = "1.0.0";
	}

	void ARC::destroy()
	{
	}

	void ARC::createRubyInterface()
	{
		rb_mARC = rb_define_module("ARC");
		rb_define_const(rb_mARC, "Version", rb_str_new2(Version.c_str()));
		rb_define_module_function(rb_mARC, "system_path", RUBY_METHOD_FUNC(&ARC::rb_getSystemPath), 0);
		rb_define_module_function(rb_mARC, "cfg_parameters", RUBY_METHOD_FUNC(&ARC::rb_getCfgParameters), 0);
		rb_define_module_function(rb_mARC, "backend_id", RUBY_METHOD_FUNC(&ARC::rb_getBackendId), 0);
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE ARC::rb_getSystemPath(VALUE self)
	{
		return rb_str_new2(reactor::system->Path.c_str());
	}

	VALUE ARC::rb_getCfgParameters(VALUE self)
	{
		VALUE result = rb_hash_new();
		foreach_m (hstr, it, reactor::system->Parameters)
		{
			rb_hash_aset(result, rb_str_new2(it->first.c_str()), rb_str_new2(it->second.c_str()));
		}
		return result;
	}

	VALUE ARC::rb_getBackendId(VALUE self)
	{
		return UINT2NUM((unsigned int)april::window->getBackendId());
	}

}
