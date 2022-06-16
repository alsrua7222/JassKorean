def isMPQ(file: str):
    if file.endswith('.mpq') or file.endswith('.w3x') or file.endswith('.w3m'):
        return True
    return False