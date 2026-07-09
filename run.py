try:
    import main
    if hasattr(main, 'main'):
        main.main()
    else:
        print("Modul berhasil di-import, tapi fungsi 'main()' tidak ditemukan.")
except Exception as e:
    print(f"Ada error, sayang: {e}")

