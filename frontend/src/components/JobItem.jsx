import { Link } from "react-router-dom";

export default function JobItem({job}){

    return (
        <li key={job.id}>
            <Link to={`/jobs/${job.id}`} >{job.title}</Link>
            <p>Location: {job.location}</p>
            <p>{job.job_type}</p>
        </li>
    )
}