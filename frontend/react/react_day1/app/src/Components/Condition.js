import React from 'react'

function Condition(props) {
    return (
        <div>
            {props.logged == "1" ? (
                <div>
                    {props.name == 'admin' ? (<h1>Welcome {props.name}</h1>) : (<h1>Welcome Customer</h1>)}
                </div>

            ) : (
                <h1>login to continue</h1>
            )}
        </div>
    )
}

export default Condition