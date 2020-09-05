let sequence = {
    'Arad' : ['Timisoara','Zerind','Sibiu'],
    'Timisoara' : ['Lugoj'],
    'Zerind': ['Orada'],
    'Orada' : ['Sibiu'],
    'Lugoj' : ['Mehadia'],
    'Mehadia' : ['Drobeta'],
    'Drobeta' : ['Craiova'],
    'Craiova' : ['Rimnicu','Pitesti'],
    'Rimnicu' : ['Pitesti',],
    'Pitesti' : ['Bucharest'],
    'Bucharest' : ['Giurgiu','Urziceni'],
    'Sibiu' : ['Rimnicu','Fagaras'],
    'Fagaras' : ['Bucharest'],
    'Urziceni' : ['Hirsova','Vaslui'],
    'Hirsova' : ['Erfoie'],
    'Vaslui' : ['Iasi'],
    'Iasi' : ['Neamt'],
    'Giurgiu' : [],
    'Erfoie' : [],
    'Neamt' : [],
}

let source = document.getElementById('source')
let target = document.getElementById('target')
let solve_button = document.getElementById('solve')
let algorithm_select = document.getElementById('algorithm_select')
let circle_source_1 = document.getElementById('test11')
let circle_source_2 = document.getElementById('test12')
let circle_target_1 = document.getElementById('test21')
let circle_target_2 = document.getElementById('test22')

function ignoreerror()
{
   return true
}


//vars
let source_name = 'Arad'
let target_name = 'Bucharest'
let algorithm = 'dfs'
let result = []


//event listeners
source.addEventListener('change',changeSource);
target.addEventListener('change',changeTarget)
algorithm_select.addEventListener('change',selectAlgorithm)
solve_button.addEventListener('click',solveMap)

function changeSource(e) {
    resetMap()
    city_id = e.target.value
    element = document.getElementById(city_id)
    cx = element.getAttribute('cx')
    cy = element.getAttribute('cy')
    circle_source_1.setAttribute('cx',cx)
    circle_source_1.setAttribute('cy',cy)
    circle_source_2.setAttribute('cx',cx)
    circle_source_2.setAttribute('cy',cy)
    source_name = e.target.value
}

function changeTarget(e) {
    resetMap()
    target_name = e.target.id
    city_id = e.target.value
    element = document.getElementById(city_id)
    cx = element.getAttribute('cx')
    cy = element.getAttribute('cy')
    circle_target_1.setAttribute('cx',cx)
    circle_target_1.setAttribute('cy',cy)
    circle_target_2.setAttribute('cx',cx)
    circle_target_2.setAttribute('cy',cy)
    target_name = e.target.value
}

function selectAlgorithm(e) {
    algorithm = e.target.value
}

function solveMap() {
    resetMap()
    if((target_name != 'Bucharest') && (algorithm == 'astar' || algorithm == 'greedy' || algorithm == 'rbfs')) {
        alert('h_value are available only for target Bucharest')
    }
    else {
        fetch('/romania_routing/start', {  
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                source : source_name,
                target : target_name,
                algorithm : algorithm
            }),
        }).then(res => res.json())
        .then(data => {
            result = data['goal']
            console.log(result.length)
            for(i = 0;i < result.length;i++) {
                if(i != result.length - 1) {
                    current = result[i]
                    next = result[i + 1]
                    console.log(current,next)
                    let path
                    if (sequence[current].includes(next)) {
                        console.log(current + '_' + next)
                        path = document.getElementById(current + '_' + next)
                    } else {
                        console.log(next + '_' + current)
                        path = document.getElementById(next + '_' + current)
                    }
                    point = document.getElementById(current)
                    console.log(path)
                    point.style.stroke = 'red'
                    path.style.stroke = 'red'
                    X('rrrr')

                }
                else {
                    current = result[i]
                    point = document.getElementById(current)
                    point.style.stroke = 'red'
                }
            }
        
        })
    }
}

function X(s) {
    console.log(s)
}

function resetMap() {
    for(i = 0;i < result.length;i++) {
        if(i != result.length - 1) {
            current = result[i]
            next = result[i + 1]
            console.log(current,next)
            let path
            if (sequence[current].includes(next)) {
                path = document.getElementById(current + '_' + next)
            } else {
                path = document.getElementById(next + '_' + current)
            }

            point = document.getElementById(current)
            console.log(path)
            point.style.stroke = 'black'
            path.style.stroke = 'black'

        }
        else {
            current = result[i]
            point = document.getElementById(current)
            point.style.stroke = 'black'
        }
}

}