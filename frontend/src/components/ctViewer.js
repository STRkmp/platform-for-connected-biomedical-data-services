import React, { useState, useEffect } from "react";
import { DicomViewer, Viewport, Toolbar } from "react-dicom-viewer";

const CTViewer = () => {
    const [dicomImage, setDicomImage] = useState(null);

    useEffect(() => {
        const url = "https://my-dicom-server.com/dicom-image.dcm";
        fetch(url)
            .then((response) => response.blob())
            .then((blob) => setDicomImage(blob));
    }, []);

    return (
        <DicomViewer requestType={}>
            <Viewport imageData={dicomImage} />
            <Toolbar />
        </DicomViewer>
    );
}

export default CTViewer;
