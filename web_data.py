import os
from urllib.parse import urlparse

# Version and repository info
web_version_latest_v2 = '3.0.0'
web_version_supported_v2 = '3.0.0'
web_repository = 'https://github.com/MadMax1960/Persona.PrerequisiteInstaller/releases/latest'

# Terms of use
web_terms = '''
=====TERMS OF USE=====

Based on the GNU Affero General Public License (AGPL), version 3:

THIS PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.
SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

IN NO EVENT WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED IN
THE LICENSE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED
INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

======================

By accepting these terms, you also agree to the Microsoft Software License Terms and the .NET Library EULA:
https://visualstudio.microsoft.com/license-terms/vs2022-cruntime/
https://dotnet.microsoft.com/en-us/dotnet_library_license.htm

Last updated: 31 August 2024
'''

# Installer class
'''
name: The full name of the prerequisite.
url: The URL from which to download the prerequisite.
checksum: The SHA-512 checksum of the prerequisite, provided by Microsoft.
'''
class Installer:
    def __init__(self, n, u, c):
        self.name = n
        self.url = u
        self.checksum = c

    def get_filename(self):
        return(os.path.basename(self.url))
    
    def get_host(self):
        return(urlparse(self.url).hostname)

# web_installers array
web_installers = [
    Installer('Visual C++ x64 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x64.exe', '4db5078fdd9eb9ce00a1b6195a67c779a1d3c719de0fbd4729adbdac2d8ca442cf4e0a31aa40d213f29617ec073f1a7e42570dcc2f931eb9534c45f1ec6de253'),
    Installer('Visual C++ x86 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x86.exe', '8a0991b993d5206450228454b4f83251cc311cc2b0dd105494928e03bf2e865de8ccf9676c8e7453164bb1805929a3a9616ea020524b77dbc0a6bbca0d222daf'),
    Installer('.NET 9.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/685792b6-4827-4dca-a971-bce5d7905170/1bf61b02151bc56e763dc711e45f0e1e/windowsdesktop-runtime-9.0.0-win-x64.exe', 'e48e015327598623cac9081a556f76f4d4d74c33e35a7cecbd2989a5b2bcb6575017e922883fc841e10efdec3d9577a47ed2b036b7f431d8f8442bb1066e72ac'),
    Installer('.NET 9.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/8dfbde7b-c316-418d-934a-d3246253f342/69c6a35b77a4f01b95588e1df2bddf9a/windowsdesktop-runtime-9.0.0-win-x86.exe', 'f597d55205b776391ac1aeb56c40abf5274e6473193c4e6c48982582c135db199d8e75adba87bdacca8981752f04f596105548ab9cc267139e681c7858890543')
]
