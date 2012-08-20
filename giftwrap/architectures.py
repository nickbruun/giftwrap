ARCHITECTURE_ANY = 'any'
"""Any architecture.

Specifying only any indicates that the source package isn't dependent on any 
particular architecture and should compile fine on any one. The produced binary 
package(s) will be specific to whatever the current build architecture is.
"""


ARCHITECTURE_ALL = 'all'
"""All architecures.

Specifying only all indicates that the source package will only build 
architecture-independent packages.
"""


ARCHITECTURE_ARMHF = 'armhf'
"""Hard-float ARM.
"""


ARCHITECTURE_ARMEL = 'armel'
"""Little endian ARM.
"""


ARCHITECTURE_POWERPCSPE = 'powerpcspe'
"""PowerPC Signal Processing Engine.
"""


ARCHITECTURE_LPIA = 'lpia'
"""Low-Power Intel Architecture.
"""


ARCHITECTURE_I386 = 'i386'
"""Intel x86.
"""


ARCHITECTURE_IA64 = 'ia64'
"""Intel Itanium.
"""


ARCHITECTURE_ALPHA = 'alpha'
"""Alpha.
"""


ARCHITECTURE_AMD64 = 'amd64'
"""AMD 64 (x64).
"""


ARCHITECTURE_ARMEB = 'armeb'
"""Big endian ARM.
"""


ARCHITECTURE_ARM = 'arm'
"""Little endian ARM.
"""


ARCHITECTURE_AVR32 = 'avr32'
"""AVR32.
"""


ARCHITECTURE_HPPA = 'hppa'
"""Hewlett Packard Precision Architecture.
"""


ARCHITECTURE_M32R = 'm32r'
"""M32R.
"""


ARCHITECTURE_M68K = 'm68k'
"""Motorola 68000 series instruction set.
"""


ARCHITECTURE_MIPS = 'mips'
"""Big endian MIPS.
"""


ARCHITECTURE_MIPSEL = 'mipsel'
"""Little endian MIPS.
"""


ARCHITECTURE_POWERPC = 'powerpc'
"""PowerPC.
"""


ARCHITECTURE_PPC64 = 'ppc64'
"""64-bit PowerPC.
"""


ARCHITECTURE_S390 = 's390'
"""IBM ESA/390.
"""


ARCHITECTURE_S390X = 's390x'
"""Extended IBM ESA/390.
"""


ARCHITECTURE_SH3 = 'sh3'
"""Little endian SH-3 (SuperH).
"""


ARCHITECTURE_SH3EB = 'sh3eb'
"""Big endian SH-3 (SuperH).
"""


ARCHITECTURE_SH4 = 'sh4'
"""Little endian SH-4 (SuperH).
"""


ARCHITECTURE_SH4EB = 'sh4eb'
"""Big endian SH-4 (SuperH).
"""


ARCHITECTURE_SPARC = 'sparc'
"""SPARC.
"""


ARCHITECTURE_SPARC64 = 'sparc64'
"""64-bit SPARC.
"""
