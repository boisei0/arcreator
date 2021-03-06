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
/// Represents a linear force affector.

#ifndef APRILPARTICLE_LINEAR_FORCE_H
#define APRILPARTICLE_LINEAR_FORCE_H

#include <gtypes/Vector3.h>
#include <hltypes/harray.h>
#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>

#include "Affector.h"

namespace aprilparticle
{
	class Particle;

	namespace Affectors
	{
		class aprilparticleExport LinearForce : public Affector
		{
		public:
			LinearForce(chstr name = "");
			LinearForce(gvec3 direction, chstr name = "");
			~LinearForce();
			static Affector* createInstance(chstr name = "");
			
			HL_DEFINE_GETSET(gvec3, direction, Direction);
			inline void setDirection(float x, float y, float z) { this->direction.set(x, y, z); }

			harray<PropertyDescription> getPropertyDescriptions();

			hstr getProperty(chstr name);
			bool setProperty(chstr name, chstr value);

			void update(Particle* particle, float timeDelta, gvec3& movement);

		protected:
			gvec3 direction;
	
		private:
			static harray<PropertyDescription> _propertyDescriptions;

		};
	};
}

#endif
