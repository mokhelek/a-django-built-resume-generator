
function full_detailsFunction(){
    let full_details = document.getElementById("full_details")
    let personal_info = document.getElementById("personal_info")
    let experiences = document.getElementById("experiences")
    let education = document.getElementById("education")

    if (full_details.style.display=="none"){
        full_details.style.display = "block"    
        education.style.display = 'none'
        experiences.style.display = 'none'
        personal_info.style.display = "none"
   
        }
}

function personalFunction(){
    let full_details = document.getElementById("full_details")
    let personal_info = document.getElementById("personal_info")
    let experiences = document.getElementById("experiences")
    let education = document.getElementById("education")

    if (personal_info.style.display=="none"){
        personal_info.style.display = "block"
        experiences.style.display = 'none'
        education.style.display = 'none'
        full_details.style.display = "none"

    }

}

function experiencesFunction(){
    let full_details = document.getElementById("full_details")
    let personal_info = document.getElementById("personal_info")
    let experiences = document.getElementById("experiences")
    let education = document.getElementById("education")

    if (experiences.style.display=="none"){
        experiences.style.display = 'block'
        personal_info.style.display = "none"
        education.style.display = 'none'

        full_details.style.display = "none"
 
        }
}



function educationFunction(){
    let full_details = document.getElementById("full_details")
    let personal_info = document.getElementById("personal_info")
    let experiences = document.getElementById("experiences")
    let education = document.getElementById("education")

    if (education.style.display=="none"){
        education.style.display = 'block'
        experiences.style.display = 'none'
        personal_info.style.display = "none"
    
        full_details.style.display = "none"
    
        }
}


