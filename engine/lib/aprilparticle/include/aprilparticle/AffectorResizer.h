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
/// Represents a resizing affector.

#ifndef APRILPARTICLE_RESIZER_H
#define APRILPARTICLE_RESIZER_H

#include <gtypes/Vector2.h>
#include <hltypes/harray.h>
#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>

#include "Affector.h"

namespace aprilparticle
{
	class Particle;

	namespace Affectors
	{
		class aprilparticleExport Resizer : public Affector
		{
		public:
			Resizer(chstr name = "");
			Resizer(gvec2 startSize, gvec2 endSize, chstr name = "");
			~Resizer();
			static Affector* createInstance(chstr name = "");

			HL_DEFINE_GETSET(gvec2, startSize, StartSize);
			inline void setStartSize(float x, float y) { this->startSize.set(x, y); }
			HL_DEFINE_GETSET(gvec2, endSize, EndSize);
			inline void setEndSize(float x, float y) { this->endSize.set(x, y); }
				
			harray<PropertyDescription> getPropertyDescriptions();

			hstr getProperty(chstr name);
			bool setProperty(chstr name, chstr value);

			void update(Particle* particle, float timeDelta, gvec3& movement);

		protected:
			gvec2 startSize;
			gvec2 endSize;

		private:
			static harray<PropertyDescription> _propertyDescriptions;

			float _ratio;

		};
	};
}

#endif
