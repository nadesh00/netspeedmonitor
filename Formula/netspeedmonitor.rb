class Netspeedmonitor < Formula
  include Language::Python::Virtualenv

  desc "Network speed monitor for macOS menu bar"
  homepage "https://github.com/nadesh00/netspeedmonitor"
  url "https://github.com/nadesh00/netspeedmonitor/archive/refs/tags/v1.1.0.tar.gz"
  sha256 "49bc28cbac94ef1edc5af63336d1b41d5231cc698dd3ca16e0f7cd1e37a72944"
  license "MIT"

  depends_on "python@3.11"

  def install
    virtualenv_install_with_resources
  end

  # We would normally list all dependencies here as resources for a completely offline install,
  # but for a custom tap, we can also simplify or use a Cask for the .app bundle.

  test do
    system "true"
  end
end
