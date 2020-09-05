print = console.log

class Stack {

    constructor() {
        this.stack = []
        this.len = 0
    }

    push(element) {
        this.stack.push(element)
        this.len += 1
    }

    pop() {
        if(this.len > 0) {
            let temp = this.stack[this.len - 1]
            this.stack.splice(this.len - 1,1)
            this.len -= 1
            return temp
        }
        else {
            return null
        }
    }

    top() {
        return self.stack[len - 1]
    }
}

class Queue {
    
    constructor() {
        this.queue = []
        this.len = 0
    }

    addQueue(item) {
        this.queue.push(item)
        this.len += 1
    }

    deQueue() {
        if(this.len == 0)
            return null
        let temp = this.queue[0]
        this.queue.splice(0,1)
        this.len -= 1
        return temp
    }

}

class CSPNode{
    constructor(assignments,domains,degree_of_unassigned_vars,unassigned_vars) {
        this.assignments = assignments
        this.domains = domains
        this.unassigned_vars = unassigned_vars
        this.degree_of_unassigned_vars = degree_of_unassigned_vars
    }
}




class CSP {

    constructor(graph,initial_state,domain_count,MRV_heuristic=false,degree_heuristic=false,lcv_heuristic=false,forward_checking=false,arc_consistency=false) {
        this.graph = graph
        this.MRV_heuristic = MRV_heuristic
        this.degree_heuristic = degree_heuristic
        this.lcv_heuristic = lcv_heuristic
        this.forward_checking = forward_checking
        this.arc_consistency = arc_consistency
        this.stack = new Stack()
        this.stack.push(initial_state)
        this.domain_count = domain_count
        this.edges = []
        for(const [key,values] of Object.entries(this.graph)) {
            this.nodes.push(key)
            for(value of values) {
                this.edges.push([key,value])
            }
        }

    }



    run() {
        while(true) {
            let element = this.stack.pop()
            //ricieve cspnode get next node name to give value
            let variable = this.getNextVar(element)
            if(this.lcv_heuristic) {
                
            }
            else {
                for(domain of element.domains[variable]) {
                    x = this.makeCopyOfCSPNode(element)
                    x.domains[variable] = domain
                    x.assignments[variable] = domain
                    if(this.arc_consistency) {
                        let res, x_new = this.arcConsistency(x,variable)
                        if(res == true)
                            x_new.unassigned_vars = element.unassigned_vars - 1
                            this.stack.push(x_new)
                    }
                    else if(this.forward_checking) {
                        let res, x_new = this.forwardCheking(x,variable)
                        if(res == true)
                            x_new.unassigned_vars = element.unassigned_vars - 1
                            for(adjacent of this.graph[variable]) {
                                if(x_new.assignments[adjacent] == null)
                                    x_new.degree_of_unassigned_vars[adjacent] -= 1
                            }
                            this.stack.push(x_new)                     
                    }
                    else {
                        let res, x_new = this.checkValidityWithNoHeuristic(x,variable)
                        if(res == true)
                            x_new.unassigned_vars = element.unassigned_vars - 1
                            this.stack.push(x_new)  
                    }

                    if(this.checkGoal(x_new)) {
                        return x_new.assignments
                    }
                }
            }
        }
    }



    getNextVar(element) {
        let variable = null
        if(this.MRV_heuristic) {
            let temp = this.MRV(element)
            if((temp.length > 1) && this.degree_heuristic) {
                variable = this.degree(element,temp)
            }
            else if((temp.length > 1) && !this.degree_heuristic) {
                variable = temp[0]
            }
            else if(temp.length == 1) {
                variable = temp[0]
            }
        }
        else if(this.degree_heuristic){
            variable = this.degree(element)
        }
        else {
            for(const [key,value] of Object.entries(element.assignments)) {
                if(value == null) {
                    variable = key
                    break
                }
            }
        }

        return variable
    }



    MRV(element) {
        let temp = []
        let min_domain_choice = this.domain_count
        for(const [key,values] of Object.entries(element.domains)) {
            if(values.length < min_domain_choice) {
                temp = []
                min_domain_choice = values.length
                temp.push(key)
            }
            else if(value == min_domain_choice) {
                temp.push(key)
            }
        }

        return temp
    }

    degree(element,candidates=null) {
        let max_value = 0
        let id_of_candidate = null
        if(candidates != null) {
            for(candidate of candidates) {
                if(element.degree_of_unassigned_vars[candidate] > max_value) {
                    max_value = element.degree_of_unassigned_vars[candidate]
                    id_of_candidate = candidate
                }
            }
        }
        else {
            for(id_ of this.graph[ids]) {
                if(element.assignments[id_] == null)
                    if(element.degree_of_unassigned_vars[candidate] > max_value)
                        max_value = element.degree_of_unassigned_vars[candidate]
                        id_of_candidate = id_                      
            }
        }
        return id_of_candidate
    }
    


    lcv(element) {

    }

    arcConsistency(x,variable) {
        let edge_queue = Queue()
        for(edge of this.edges) {
            edge_queue.addQueue(edge)
        }
        while(true) {
            let arc = edge_queue.deQueue()
            if(arc == null) 
                return true, x
            if(this.removeInconsistentDomains(x,arc[0],arc[1])) {
                if(x.domains[arc[0]] == [])
                    return false, x
                for(adjacent of graph[arc[0]]) {
                    edge_queue.addQueue([adjacent,arc[0]])
                }
            }
        }
    }

    forwardCheking(x,variable) {
        for(adjacent of this.graph[variable]) {
            let value = x.assignments[variable]
            if(x.domains[adjacent].includes(value)) {
                let index = x.domains[adjacent].indexOf(value)
                x.domains[adjacent].splice(index,1)
                if(x.domains[adjacent] == [])
                    return false, x
            }
        }
        return true, x
    }

    checkValidityWithNoHeuristic(x,variable) {
        let value = x.assignments[variable]
        for(adjacent of this.graph[variable]) {
            if(x.assignments[variable] == x.assignments[adjacent])
                return false, x
        }
        return true, x
    }

    checkGoal(x_new) {
        if(x_new.unassigned_vars == 0)
            return true
        else
            return false
    }

    makeCopyOfCSPNode(node) {
        let assignments_copy = Object.assign({},node.assignments)
        let domains_copy = Object.assign({},node.domains)
        let degree_of_unassigned_vars_copy = Object.assign({},node.degree_of_unassigned_vars)
        let unassigned_vars_copy = node.unassigned_vars
        let node_copy = new CSPNode(assignments_copy,domains_copy,degree_of_unassigned_vars_copy,unassigned_vars_copy)
        return node_copy
    }

    removeInconsistentDomains(x,node_1,node_2) {
        let final_res = false
        let res = null
        let remove_candidates  = []
        let index = null
        for(domain_1 of x.domains[node_1]) {
            res = false
            for(domain_2 of x.domains[node_2]) {
                if(domain_1 != domain_2)
                    res = true
            }
            if(res != true) {
                remove_candidates.push(domain_1)
                final_res = true
            }
        }
        for(doamin of remove_candidates) {
            index = x.domains[node_1].indexOf(domain)
            x.domains[node_1].splice(index,1)
        }
        return final_res
    }
}