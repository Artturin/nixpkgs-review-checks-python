with import <nixpkgs> { };

mkShell rec {
  # include any libraries or programs in buildInputs
  buildInputs = let 
    pythonPackages = pythonPackages: with pythonPackages; [
      setuptools
      requests
      jq
      PyGithub

    ];
  in 
  with pkgs; [
    (python3.withPackages pythonPackages)
    cached-nix-shell
    gh

  ];

  # shell commands to be ran upon entering shell
  shellHook = ''
  '';
}
