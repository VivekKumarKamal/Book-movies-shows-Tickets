function deleteVenue(venueId){
    if (confirm("Are you sure you want to delete this Venue")){
        fetch(`/delete-venue/${venueId}`,
        {method: "POST"})
        .then((_res) =>{
                window.location.href ="/";
        });
    }
}
function deleteShow(showId){
    if (confirm("Are you sure you want to delete this Show")){
        fetch(`/delete-show/${showId}`,
        {method: "POST"})
        .then((_res) =>{
                window.location.href ="/";
        });
    }
}