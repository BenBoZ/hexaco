"""

    This file is part of HexACO.

    HexACO is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    HexACO is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with HexACO.  If not, see <http://www.gnu.org/licenses/>.

########################################################################

Common library

########################################################################

Description
-----------
Module that contains all global settings """

# The size of a tile, which also infuences the size of the other objects
HEX_RADIUS = 8

# The number of rings of which the map is constructed
MAPSIZE = 20

# The precision used when comparing ints and floats
EPSILON = 1.0e-3

# Ants
NUMBER_OF_ANTS = 50
PIECES_OF_FOOD = 15

ANT_DEFAULTS = {'SPEED':0.25, 'DEPOSIT_FOOD':75, 'DEPOSIT_HOME':25}