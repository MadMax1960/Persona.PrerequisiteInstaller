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
    Installer('.NET 9.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/084bfbb9-6197-49d9-ae9c-ad3825534f37/e1a071d344c9b24849f8034f7ce72aa6/dotnet-sdk-9.0.100-rc.2.24474.11-win-x64.exe', '29091a2b4d08f7fdc77065f2805a82afae0129a6b886caec71124016843a29c6abcec828794aef1c9a73a84df3f7b7258863991f61a780ea362575da0ca6879b'),
    Installer('.NET 9.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/d052307a-2d94-4192-935c-b6586e7077d2/3e3dfc72d4bf97bf2d6281ef250114d2/dotnet-sdk-9.0.100-rc.2.24474.11-win-x86.exe', '42622d7145da2cd246c4490213ba0fd9e9a8c4f567a0f6b940f24029a6f342264be6b3f65ea79b46ee4048a7d74201d25ba98402ce4c245f82ee318f5442af1c')
]
