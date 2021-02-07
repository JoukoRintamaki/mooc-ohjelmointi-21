def ilman_vokaaleja(merkkijono):
    for i in "aeiouyåäö":
        merkkijono = merkkijono.replace(i, '')
    return merkkijono