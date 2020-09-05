let puzzle_generator = document.getElementById('puzzle_generator')
let solve_button = document.getElementById('solve')
let forward_checking_checkbox = document.getElementById('forward_checking')
let arc_consistency_checkbox = document.getElementById('arc_consistency')
let mrv_checkbox = document.getElementById('mrv')
let degree_checkbox = document.getElementById('degree')
let lcv_checkbox = document.getElementById('lcv')
let end = document.getElementById('end')

let forward_checking = forward_checking_checkbox.checked
let arc_consistency = arc_consistency_checkbox.checked
let mrv = mrv_checkbox.checked
let degree = degree_checkbox.checked
let lcv = lcv_checkbox.checked
let interval = 100
let timer
let is_puzzle_generated = false
let initial_table

puzzle_generator.addEventListener('click',generatePuzzle)
solve_button.addEventListener('click',solvePuzzle)
forward_checking_checkbox.addEventListener('change',changeForwardCheck)
arc_consistency_checkbox.addEventListener('change',changeArcConsistency)
mrv_checkbox.addEventListener('change',changeMRV)
degree_checkbox.addEventListener('change',changeDegree)
lcv_checkbox.addEventListener('change',changeLCV)
end.addEventListener('click',endAlgorithm)


function solvePuzzle() {
    if(is_puzzle_generated) {
        timer = setInterval(getPuzzle,interval)
        fetch('/sudoku/start', {  
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                forward_checking : forward_checking,
                arc_consistency : arc_consistency,
                mrv : mrv,
                degree : degree,
                lcv : lcv,
                initial_table : initial_table,
            })
        })
    }
}

function generatePuzzle() {
        clearPuzzle()
        fetch('/sudoku/generate')
        .then(res => res.json())
        .then(data => {
            let table = data['table']
            console.log(table)
            initial_table = table
            for(i = 0;i < table.length;i++) {
                for(j = 0;j < table.length;j++) {
                    if(table[i][j] != 'X') {
                        document.getElementById('A_' + i + j).innerHTML = table[i][j]
                    }
                }
            }
        })
        is_puzzle_generated = true
    }

function endAlgorithm() {
    clearInterval(timer)
    fetch('/sudoku/stop')
    clearPuzzle()
}

function getPuzzle() {
    fetch('/sudoku/getpuzzle')
    .then(res => res.json())
    .then(data => {
        let table = data['table']
        let done = data['done']
        let have_answer = data['have_answer']
        for(const [key,value] of Object.entries(table)) {
            if(value != null) {
                document.getElementById(key).innerHTML = value
            }
        }
        if(done == true) {
            clearInterval(timer)
        }
        if(!have_answer) {
            clearInterval(timer)
        }
    })
}

function changeForwardCheck() {
    forward_checking = !forward_checking
}

function changeArcConsistency() {
    arc_consistency = !arc_consistency
}

function changeMRV() {
    mrv = !mrv
}

function changeDegree() {
    degree = !degree
}

function changeLCV() {
    lcv = lcv
}

function clearPuzzle() {
    initial_table = []
    for(i = 0;i < 9;i++) {
        for(j = 0;j < 9;j++) {
                document.getElementById('A_' + i + j).innerHTML = ''
            }
        }
    }

