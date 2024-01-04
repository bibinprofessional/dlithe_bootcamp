import React from 'react'

function CheckPositive(props) {
    return (
        <div>
            {Number(props.number) > 0 ? (
                <h2>number : {props.number}</h2>
            ) : (
                <div>
                    <h2>number : {props.number}</h2>
                    <h2>The given number is negative</h2>
                </div>

            )
            }
        </div>
    )
}

export default CheckPositive