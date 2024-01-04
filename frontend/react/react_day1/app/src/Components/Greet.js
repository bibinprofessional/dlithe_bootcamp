import React from 'react'

const Greet = (props) => {
    return (
        <div>
            hello team, I am {props.name}, {props.age} years old.
        </div>
    )
}

export default Greet