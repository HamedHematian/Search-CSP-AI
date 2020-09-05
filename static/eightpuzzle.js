let solve_button = document.getElementById('solve')
let algorithm_select = document.getElementById('algorithm_select')
let puzzle_generator = document.getElementById('puzzle_generator')
let main_div = document.getElementById('main')
let pause_resume_button = document.getElementById('pause_resume')



//vars
let algorithm = algorithm_select.value
let result = null
let initial_state = null
let is_puzzle_generated = false
let counter = 0
let paused = false

print = console.log

//event listeners
algorithm_select.addEventListener('change',selectAlgorithm)
solve_button.addEventListener('click',solvePuzzle)
puzzle_generator.addEventListener('click',generatePuzzle)
pause_resume_button.addEventListener('click',pauseAndResume)

// function moveTop(num) {
//     temp = document.getElementById(num)
//     temp.style.bottom += '97px'
// }

// function moveBottom(num) {
//     temp = document.getElementById(num)
//     temp.style.top += '97px'
// }

// function moveRight(num) {
//     temp = document.getElementById(num)
//     temp.style.left += '97px'
// }

// function moveLeft(num) {
//     temp = document.getElementById(num)
//     temp.style.right += '97px'
// }

// function solvePuzzle(e) {
//     fetch('/eight_puzzle/start', {  
//         method: 'POST',
//         headers: {'Content-Type': 'application/json'},
//         body: JSON.stringify({
//             initial_state : initial_state,
//             algorithm : algorithm
//         }),
//     }).then(res => res.json())
//       .then(data => {
//         console.log(data)
//     }
// }
        
function pauseAndResume() {
    console.log('yesssss')
    if(paused == false) {
        fetch('/eight_puzzle/pause')
        .then(res => res.json())
        .then(data => console.log(data))
        paused = true

    }
    else {
        fetch('/eight_puzzle/resume')
        paused = false
    }
}


function generatePuzzle(e) {
    main_div.innerHTML = ''
    fetch('/eight_puzzle/generate')
    .then(res => res.json())
    .then(data => {
        let table_data = data['table']
        initial_state = table_data
        table = document.createElement('table')
        for(i = 0;i < 3;i++){
            let tr = document.createElement('tr')
            table.appendChild(tr)
            for(j = 0;j < 3;j++) {
                if(table_data[i][j] != 'X'){
                    td = document.createElement('td')
                    td.setAttribute('id','td_' + i + '_' + j)
                    td.innerHTML = table_data[i][j]
                    tr.appendChild(td)
                }
                else {
                    td = document.createElement('td')
                    td.setAttribute('id','td_' + i + '_' + j)
                    td.className += 'empty_td'
                    tr.appendChild(td)
                }
            }
        }
        main_div.appendChild(table)

    })
}


function selectAlgorithm(e) {
    algorithm = e.target.value
}



function solvePuzzle() {
    fetch('/eight_puzzle/start', {  
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            initial_state : initial_state,
            algorithm : algorithm
        })
    }).then(res => res.json())
      .then(data => {
        result = data['path']
        setInterval(animate,2000)
      })
    }
      


function animate() {
    print('xxxxxxx')
    for(j=0;j<3;j++){
        for(k=0;k<3;k++){
          if(result[counter][j][k] == 'X') {
            row_1 = j;col_1 = k;
            }
        }
    }

      for(j=0;j<3;j++){
        for(k=0;k<3;k++){
          if(result[counter + 1][j][k] == 'X') {
            row_2 = j;col_2 = k;
            }
        }
    }
    current = document.getElementById('td_' + row_1 + '_' + col_1)
    next = document.getElementById('td_' + row_2 + '_' + col_2)
    current.innerHTML = next.innerHTML
    // current.style.backgroundColor = 'rgb(28, 16, 78)'
    // next.style.backgroundColor = '#eee'
    next.innerHTML = ''






    //   if(row_1 != row_2) {
    //       if(row_2 == row_1 + 1) {
              
    //       }
    //       else if(row_2 == row_1 - 1) {
              
    //       }
    //   }
    //   else if(col_1 != col_2) {
    //       if(col_2 == col_1 + 1) {
              
    //       }
    //       else if(col_2 == col_1 - 1) {
             
    //       }
    //   }
    counter += 1
}