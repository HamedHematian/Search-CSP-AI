let solve_button = document.getElementById('solve')
let forward_checking_checkbox = document.getElementById('forward_checking')
let arc_consistency_checkbox = document.getElementById('arc_consistency')
let mrv_checkbox = document.getElementById('mrv')
let degree_checkbox = document.getElementById('degree')
let lcv_checkbox = document.getElementById('lcv')
let color_count_select = document.getElementById('color_count_select')
let end = document.getElementById('end')

let forward_checking = forward_checking_checkbox.checked
let arc_consistency = arc_consistency_checkbox.checked
let mrv = mrv_checkbox.checked
let degree = degree_checkbox.checked
let lcv = lcv_checkbox.checked
let map_name = window.location.href.split('/').slice(-1)[0]
let interval = 100
let color_count = 3
let timer

solve_button.addEventListener('click',solveMap)
forward_checking_checkbox.addEventListener('change',changeForwardCheck)
arc_consistency_checkbox.addEventListener('change',changeArcConsistency)
mrv_checkbox.addEventListener('change',changeMRV)
degree_checkbox.addEventListener('change',changeDegree)
lcv_checkbox.addEventListener('change',changeLCV)
color_count_select.addEventListener('change',selectColorCount)
end.addEventListener('click',endAlgorithm)

function solveMap() {
    clearMap()
    timer = setInterval(getMap,interval)
    fetch('/map/start', {  
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            forward_checking : forward_checking,
            arc_consistency : arc_consistency,
            mrv : mrv,
            degree : degree,
            lcv : lcv,
            map_name : map_name,
            color_count : color_count
        })
    })
}

function endAlgorithm() {
    clearInterval(timer)
    fetch('/map/stop')
    clearMap()
}

function getMap() {
    fetch('/map/getmap')
    .then(res => res.json())
    .then(data => {
        let states = data['map']
        let done = data['done']
        let have_answer = data['have_answer']
        for(const [key,value] of Object.entries(states)) {
            if(value != null) {
                document.getElementById(key).style.fill = value
            }
        }
        if(done == true) {
            clearInterval(timer)
        }
        if(!have_answer) {
            clearInterval(timer)
            alert('this map has no answer with this count of colors')
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
    lcv = !lcv
}


function selectColorCount(e) {
    if(e.target.value == 'four') {
        color_count = 4
    }
    else if(e.target.value == 'three') {
        color_count = 3
    }

}

function clearMap() {
    let path_array = document.getElementsByTagName('path')
    for(path of path_array) {
        path.style.fill = "#CCCCCC"
    }
}