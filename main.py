import os
import json
import ldclient

def main():
    with open('config.json', 'r') as f:
        config = json.load(f)
        ldclient.set_sdk_key(config["hoge"])

    with open('user.json', 'r') as f:
        user = json.load(f)

    show_feature = ldclient.get().variation("test-flg", user, False)
    print("show_feature %s" % show_feature)

    if show_feature:
        print("Showing your feature")
    else:
        print("Not showing your feature")

    ldclient.get().close()

if __name__ == "__main__":
    main()


