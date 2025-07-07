export default function JobDetail({job}){
    return (
        <div>
            <h2>{job.title}</h2>
            <p>{job.description}</p>
            <p>Location: {job.location}</p>
            <p>{job.job_type}</p>
        </div>
    )
}