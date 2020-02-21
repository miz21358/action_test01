import os
import json
import ldclient

def main():
    ldclient.set_sdk_key(os.environ['LD_SDK_KEY'])

    with open('user.json', 'r') as f:
        user = json.load(f)
        print(user)

    show_feature = ldclient.get().variation("test-flg", user, False)
    print("show_feature %s" % show_feature)

    state = ldclient.get().all_flags_state(user)
    print("state %s" % state.keys())

    if show_feature:
        print("Showing your feature")
    else:
        print("Not showing your feature")

    ldclient.get().close()

if __name__ == "__main__":
    main()


