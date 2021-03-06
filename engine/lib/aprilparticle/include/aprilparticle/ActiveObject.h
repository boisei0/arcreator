/// @file
/// @version 2.2
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause
/// 
/// @section DESCRIPTION
/// 
/// Represents an active object.

#ifndef APRILPARTICLE_ACTIVE_OBJECT_H
#define APRILPARTICLE_ACTIVE_OBJECT_H

#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>

#include "aprilparticleExport.h"
#include "PropertyDescription.h"

namespace aprilparticle
{
	class Affector;

	class aprilparticleExport ActiveObject
	{
	public:
		ActiveObject(chstr name = "");
		ActiveObject(const ActiveObject& other);
		virtual ~ActiveObject();

		HL_DEFINE_GETSET(hstr, name, Name);
		HL_DEFINE_ISSET(visible, Visible);
		HL_DEFINE_ISSET(enabled, Enabled);

		virtual harray<PropertyDescription> getPropertyDescriptions();
		bool hasProperty(chstr name);

		hstr getProperty(chstr name);
		bool setProperty(chstr name, chstr value);

	protected:
		hstr name;
		bool visible;
		bool enabled;

	private:
		static harray<PropertyDescription> _propertyDescriptions;

	};
}

#endif
