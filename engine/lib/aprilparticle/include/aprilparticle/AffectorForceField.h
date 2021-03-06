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
/// Represents a force field affector.

#ifndef APRILPARTICLE_FORCE_FIELD_H
#define APRILPARTICLE_FORCE_FIELD_H

#include <gtypes/Vector3.h>
#include <hltypes/harray.h>
#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>

#include "AffectorSpace.h"

namespace aprilparticle
{
	class Particle;

	namespace Affectors
	{
		class aprilparticleExport ForceField : public Space
		{
		public:
			ForceField(chstr name = "");
			ForceField(gvec3 position, float radius, gvec3 direction, chstr name = "");
			~ForceField();
			static Affector* createInstance(chstr name = "");

			HL_DEFINE_GETSET(gvec3, direction, Direction);
			inline void setDirection(float x, float y, float z) { this->direction.set(x, y, z); }
				
			harray<PropertyDescription> getPropertyDescriptions();

			hstr getProperty(chstr name);
			bool setProperty(chstr name, chstr value);

			void update(Particle* article, float timeDelta, gvec3& movement);
			void draw();

		protected:
			gvec3 direction;

		private:
			static harray<PropertyDescription> _propertyDescriptions;

			float _factor;
			float _squaredLength;
			
		};
	};
}

#endif
