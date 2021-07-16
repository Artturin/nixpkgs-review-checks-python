from nixpkgs_review.checks import checks
from nixpkgs_review.review import review
from nixpkgs_review.functions import ofborg_state
import sys
import argparse

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--review", type=int)
    parser.add_argument("--checks")
    args = parser.parse_args()

    #if args.review:
    #    print(args.review)
    #    review
    #    

    #if args.checks:
    #    checks
    #    print(args.checks)

    return args



def main():
    args = arguments()

    print(args)
    ofborg_state(args.review)

if __name__ == "__main__":
    sys.exit(main())
