{ lib, python3Packages, fetchFromGitHub }:

python3Packages.buildPythonPackage rec {
  pname = "nixpkgs-review-checks-python";
  version = "0.0.1";

  #src = fetchFromGitHub {
  #  owner = "Artturin";
  #  repo = pname;
  #  rev = "";
  #  sha256 = "0000000000000000000000000000000000000000000000000000";
  #};

  src = ./.;

  doCheck = false;
  propagatedBuildInputs = with python3Packages; [
    requests
    jq
    PyGithub
  ];

  #pythonImportsCheck = [ "CHANGE" ];

  meta = with lib; {
    #description = "CHANGE";
    #homepage = "https://github.com/CHANGE/CHANGE/";
    license = licenses.mit;
    maintainers = with maintainers; [ artturin ];
  };
}
