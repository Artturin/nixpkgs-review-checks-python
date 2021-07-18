import argparse
import sys

from nixpkgs_review.checks import checks
from nixpkgs_review.functions import *
from nixpkgs_review.review import review

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--review", type=int)
    parser.add_argument("--checks")
    args = parser.parse_args()

    return args



def main():
    args = arguments()
    PR = args.review
    print(ghapi("prstatus", PR))
    if ghapi("prstatus", PR) == "open":
        print("test")
    #print(args)
    #pr_status = ghapi("pruser", PR)
    #print(pr_status)
    #print(ofborg_state(PR))

if __name__ == "__main__":
    sys.exit(main())
