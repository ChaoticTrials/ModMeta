window.addEventListener('load', () => {
    const input = document.getElementById('mx-mods-table-search-input')
    if (input != undefined) {
        function updateSearch() {
            const term = input.value == undefined ? '' : input.value.toLowerCase().trim();
            const rows = document.getElementsByClassName('mx-wiki-search-row')
            for (row of rows) {
                const match = row.getAttribute('data-search-text')
                const visible = match == undefined || match.toLocaleLowerCase().includes(term)
                if (visible) {
                    row.classList.remove('mx-wiki-hidden')
                } else {
                    row.classList.add('mx-wiki-hidden')
                }
            }
        }
        
        input.addEventListener('keydown', e => {
            if (e.code == 'Enter') {
                e.preventDefault()
            }
        })
        
        input.addEventListener('input', updateSearch)
        input.addEventListener('change', updateSearch)
    }
})
