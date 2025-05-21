from os import system

# Chiede Username e Email
def fetch_github_info() -> tuple[str, str]:
    return ( str(input('Inserisci il tuo USERNAME github: ')).strip(), str(input('Inserisci la tua EMAIL github: ')).strip() )

# Cambia le info nel file '.gitconfig'
def change_current_info(github_info: tuple[str, str]) -> None:
    for index, command in enumerate([ 'git config user.name "', 'git config user.email "' ]):
        system(command + f'{github_info[index]}"')

def main() -> None:
    change_current_info(fetch_github_info())

if __name__ == '__main__':
    main()