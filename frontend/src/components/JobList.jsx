import JobItem from "./JobItem"


export default function JobList({jobs, isLoading}){
    return (
        <ul>
            {jobs && jobs.map(job=><JobItem job={job}/>)}
            {isLoading && <p>Loading jobs...</p>}
            {!jobs && !isLoading && <p>No jobs at the moment</p>}
        </ul>
    )
}