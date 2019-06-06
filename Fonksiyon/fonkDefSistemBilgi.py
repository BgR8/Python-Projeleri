def sistembilgi():
    import sys
    print("\nSistemde kurulu Python'un;")
    print("\tana sürüm numara:", sys.version_info.major)
    print("\talt sürüm numara:", sys.version_info.minor)
    print("\tminik sürüm numara:", sys.version_info.micro)

    print("\nKullanılan işletim sistemi;")
    print("\tadı:", sys.platform)

sistembilgi()
