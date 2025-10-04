import {
    Droppable,
    Draggable,
    DragDropContext
} from '@hello-pangea/dnd'
import { useState } from 'react'

export const Categorias = () => {
    const [items, setItems] = useState([{ id: '1', text: 'Primero' }, { id: '2', text: 'Segundo' }, { id: '3', text: 'Tercero' }])

    const reorder = (list, start, end) => {
        const result = [...list]
        const [moved] = result.splice(start, 1)
        result.splice(end, 0, moved)
        return result
    }

    const onDragEnd = (result) => {
        const { destination, source } = result
        if (!destination) return
        if (destination.index === source.index) return
        setItems(prev => reorder(prev, source.index, destination.index))
    }

    return (
        <div>
            <DragDropContext onDragEnd={onDragEnd} >
                <Droppable droppableId='list' >
                    {(provided, snapshot) => (
                        <div ref={provided.innerRef} {...provided.droppableProps} style={{
                            background: snapshot.isDraggingOver ? '#f2f6ff' : '#f7f7f7',
                            padding: 12,
                            borderRadius: 10,
                            minHeight: 60,
                        }}>
                            {items.map((item, index) => (
                                <Draggable draggableId={item.id} index={index} key={item.id}>
                                    {(provided, snapshot) => (
                                        <div ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps} style={{
                                            background: '#fff',
                                            border: '1px solid #e5e5e5',
                                            color: '#000000',
                                            borderRadius: 10,
                                            padding: '12px 14px',
                                            marginBottom: 8,
                                            boxShadow: snapshot.isDragging
                                                ? '0 6px 16px rgba(0,0,0,0.12)'
                                                : '0 1px 3px rgba(0,0,0,0.06)',
                                            cursor: 'grab',
                                            ...provided.draggableProps.style,
                                        }}>
                                            {item.text}
                                        </div>)}
                                </Draggable>
                            ))}
                            {provided.placeholder}
                        </div>
                    )}
                </Droppable>
            </DragDropContext>
        </div>
    )
}
