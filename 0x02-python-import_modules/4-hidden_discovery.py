#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for u in dir(hidden_4):
        if u[:2] != "__":
            print(u)
