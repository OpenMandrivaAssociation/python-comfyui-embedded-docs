Name:		python-comfyui-embedded-docs
Version:	0.5.12
Release:	1
Summary:	Embedded node documentation for ComfyUI
License:	GPL-3.0
Group:		Development/Python
URL:		https://github.com/Comfy-Org/embedded-docs
Source0:	https://files.pythonhosted.org/packages/source/c/comfyui-embedded-docs/comfyui_embedded_docs-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Per-node help text served by ComfyUI at /docs. Optional: ComfyUI
starts without it.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/comfyui_embedded_docs
%{py_sitedir}/comfyui_embedded_docs-*.*-info
