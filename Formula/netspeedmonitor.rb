class Netspeedmonitor < Formula
  include Language::Python::Virtualenv

  desc "Network speed monitor for macOS menu bar"
  homepage "https://github.com/nadesh00/netspeedmonitor"
  url "https://github.com/nadesh00/netspeedmonitor/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "67cc7facbb323926907b18528e284b64cd0527f8b6a0652ed4dc637aceee1be3"
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
