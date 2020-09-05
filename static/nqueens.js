let new_board = document.getElementById('board_generator')
let n_input = document.getElementById('n_input')
let table = document.getElementById('table_container')
let solve_button = document.getElementById('solve')
let algorithm_select = document.getElementById('algorithm_select')


//some vars
let is_board_generated = false
let value = null
let algorithm = algorithm_select.value
let result = null
let n = 8
let non_path_algorithms = ['hillclimbing','rrhillclimbing','genetic','localbeamsearch','simulatedannealing']


//event listeners
new_board.addEventListener('click',generateNewBoard);
solve_button.addEventListener('click',solveBoard);
algorithm_select.addEventListener('change',selectAlgorithm)




//events
function generateNewBoard() {
        table.innerHTML = ''
        tr_array = []
        n = n_input.value
        if(n > 20){
            table.setAttribute('width',600)
            table.setAttribute('height',600)
        }
        for(i = 0;i < n;i++) {
            tr = document.createElement('tr')
            tr.setAttribute('id','tr_' + i)
            for(j = 0;j < n;j++) {
                td = document.createElement('td')
                td.setAttribute('id','td_' + i + '_' + j)
                td.setAttribute('width',600/n)
                td.setAttribute('height',600/n)
                tr.appendChild(td)
            }
            table.appendChild(tr)
        

    }
        is_board_generated = true
        value = n_input.value
        console.log(algorithm_select.value)
}

function solveBoard() {
    if(!is_board_generated) {
        error()
    }
    else {
        generateNewBoard()
        fetch('/nqueens/start', {  
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                n : value,
                algorithm : algorithm
            }),
        }).then(res => res.json())
      .then(data => {
          if(non_path_algorithms.includes(algorithm)) {
            result = data['goal']
          }
          else {
            result = data['goal'][n]
          }
          for([index,val] of result.entries()) {
            img = document.createElement('img')
            img.setAttribute('width',400/n)
            img.setAttribute('height',400/n)
            x = ((600 - 400)/(n * 2)) + 'px'
            img.style.zIndex = '300'
            img.style.top = x
            img.style.left = x
            img.setAttribute('src','/static/bqueen.png')
            td = document.getElementById('td_' + index + '_' + val)
            td.appendChild(img)
        }
      })
    }
}


function error() {

}

function selectAlgorithm(e) {
    algorithm = e.target.value
}

function plotQueens(array) {
    for([index,val] of array.entries()) {
        img = document.createElement('img')
        img.setAttribute('width',400/n)
        img.setAttribute('height',400/n)
        x = ((600 - 400)/(n * 2)) + 'px'
        img.style.top = x
        img.style.left = x
        img.setAttribute('src','/static/bqueen.png')
        td = document.getElementById(td_ + index + val)
        td.appendChild(img)
    }
}