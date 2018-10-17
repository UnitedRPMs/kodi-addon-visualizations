%global debug_package %{nil}
%global gitdate 20180627   

Name:           kodi-addon-visualizations
Version:        18.0
Release:        5%{?dist}
Summary:        Kodi visualizations add-ons

Group:          Applications/Multimedia
License:        GPLv3 and GPLv2+ and LGPLv2+ and MIT
URL:            https://github.com/notspiff
Source0:	https://github.com/UnitedRPMs/kodi-addon-visualizations/releases/download/18/%{name}-18-%{gitdate}.tar.xz
Source1:        kodi-addon-visualizations.sh
Source2:        kodi-addon-visualizations.txt

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kodi-devel >= 18
BuildRequires:  platform-devel
BuildRequires:  kodi-platform-devel >= 18
BuildRequires:	libprojectM-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:	mesa-libGLU-devel
BuildRequires:	autoconf
BuildRequires:	automake

Requires:	kodi >= 17
Requires:	kodi-visualization-spectrum
Requires:	kodi-visualization-waveform
Requires:	kodi-visualization-fishbmc
Requires:	kodi-visualization-shadertoy
Requires:	kodi-visualization-projectm
#Requires:	kodi-visualization-goom
#Requires:	kodi-visualization-starburst
#Requires:	kodi-visualization-vsxu
	
%description    
This package install all Kodi visualizations addons.

#----------

%package -n     kodi-visualization-spectrum
Summary:        Spectrum visualizer for Kodi
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0


%description -n kodi-visualization-spectrum
Spectrum visualizer for Kodi.

#----------

%package -n     kodi-visualization-waveform
Summary:        Waveform visualizer for Kodi
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0

%description -n kodi-visualization-waveform
Waveform visualizer for Kodi.

#----------

%package -n     kodi-visualization-fishbmc
Summary:        Fishbmc visualizer for Kodi
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0

%description -n kodi-visualization-fishbmc
Fishbmc visualizer for Kodi.

#----------

%package -n     kodi-visualization-shadertoy
Summary:        shadertoy visualizer for Kodi
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0

%description -n kodi-visualization-shadertoy
shadertoy visualizer for Kodi.

#----------

%package -n     kodi-visualization-projectm
Summary:        projectm visualizer for Kodi
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0

%description -n kodi-visualization-projectm
projectm visualizer for Kodi.

#----------

#%package -n     kodi-visualization-goom
#Summary:        goom visualizer for Kodi
#Group:          Applications/Multimedia
#Requires:       kodi  >= 17.0

#%description -n kodi-visualization-goom
#goom visualizer for Kodi.

#----------

#%package -n     kodi-visualization-starburst
#Summary:        starburst visualizer for Kodi
#Group:          Applications/Multimedia
#Requires:       kodi  >= 17.0

#%description -n kodi-visualization-starburst
#starburst visualizer for Kodi.

#----------

#%package -n     kodi-visualization-vsxu
#Summary:        vsxu visualizer for Kodi
#Group:          Applications/Multimedia
#Requires:       kodi  >= 17.0

#%description -n kodi-visualization-vsxu
#vsxu visualizer for Kodi.

%prep
%setup -n kodi-addon-visualizations 

# Fix spurious-executable-perm on debug package
find . -name '*.h' -or -name '*.cpp' | xargs chmod a-x

%build

#FIX ME
#%if 0%{?fedora} >= 26
rm -rf visualization.goom/
rm -rf visualization.starburst/
rm -rf visualization.vsxu/
#%endif

ls -d */ | sed 's:/::g' | tee addons.txt

file=addons.txt
while IFS= read -r line; do
        # display $line or do something with $line
    mkdir -p $line/build/ 
pushd %{_builddir}/kodi-addon-visualizations/$line/build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi -DBUILD_SHARED_LIBS=1 ..
make 
popd  
done <"$file"


%install
file=addons.txt
while IFS= read -r line; do
        # display $line or do something with $line
pushd %{_builddir}/kodi-addon-visualizations/$line/build
export PKG_CONFIG_PATH=%{_sourcedir}:%{_libdir}/pkgconfig
make install DESTDIR=%{buildroot}
popd  
done <"$file"


install -dm 755 %{buildroot}/%{_datadir}/licenses/
install -m644 %{S:2} %{buildroot}/%{_datadir}/licenses/

# Fix permissions at installation
find $RPM_BUILD_ROOT%{_datadir}/kodi/addons/ -type f -exec chmod 0644 {} \;

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files 
%{_datadir}/licenses/%{name}.txt


%files -n kodi-visualization-spectrum
%{_libdir}/kodi/addons/visualization.spectrum/
%{_datadir}/kodi/addons/visualization.spectrum/


%files -n kodi-visualization-waveform
%{_libdir}/kodi/addons/visualization.waveform/
%{_datadir}/kodi/addons/visualization.waveform/


%files -n kodi-visualization-fishbmc
%{_libdir}/kodi/addons/visualization.fishbmc/
%{_datadir}/kodi/addons/visualization.fishbmc/


%files -n kodi-visualization-shadertoy
%{_libdir}/kodi/addons/visualization.shadertoy/
%{_datadir}/kodi/addons/visualization.shadertoy/


%files -n kodi-visualization-projectm
%{_libdir}/kodi/addons/visualization.projectm/
%{_datadir}/kodi/addons/visualization.projectm/


#%files -n kodi-visualization-goom
#%{_libdir}/kodi/addons/visualization.goom/
#%{_datadir}/kodi/addons/visualization.goom/

#%files -n kodi-visualization-starburst
#%{_libdir}/kodi/addons/visualization.starburst/
#%{_datadir}/kodi/addons/visualization.starburst/

#%files -n kodi-visualization-vsxu
#%{_libdir}/kodi/addons/visualization.vsxu/
#%{_datadir}/kodi/addons/visualization.vsxu/

%changelog

* Sat Oct 13 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-5  
- Automatic Mass Rebuild

* Wed Sep 05 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-4  
- Automatic Mass Rebuild

* Wed Jun 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-3  
- Updated to current commit 

* Fri Apr 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-2  
- Automatic Mass Rebuild

* Wed Mar 21 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 18.0-1
- Updated to 18.0

* Sun Oct 22 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 17.5-1
- Updated to 17.5

* Fri Sep 01 2017 David Vasquez <davidva at tutanota dot com> - 17.4-2
- Rebuilt for Kodi cmake

* Mon Jun 26 2017 David Vasquez <davidva at tutanota dot com> - 17.3-1
- Initial build rpm
