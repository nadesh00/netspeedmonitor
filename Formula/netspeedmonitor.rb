class Netspeedmonitor < Formula
  include Language::Python::Virtualenv

  desc "Network speed monitor for macOS menu bar"
  homepage "https://github.com/YOUR_USERNAME/netspeedmonitor"
  url "https://github.com/YOUR_USERNAME/netspeedmonitor/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "REPLACE_THIS_WITH_ACTUAL_SHA256_AFTER_RELEASE"
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
