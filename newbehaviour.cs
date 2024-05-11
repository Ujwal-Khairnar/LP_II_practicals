using System.Collections;
using UnityEngine;
using UnityEngine.UI;

public class NewBehaviourScript : MonoBehaviour
{
    [SerializeField] 
    private GameObject Cube;
    private Renderer CubeRenderer; 
    private Transform CubeTransform; 

    private bool isRotating = false;
    private Coroutine rotationCoroutine;

    private void Start()
    {
        CubeRenderer = Cube.GetComponent<Renderer>(); 
        
        CubeTransform = Cube.transform; 
        gameObject.GetComponent<Button>().onClick.AddListener(OnChangeButtonClick);
    }

    private void OnChangeButtonClick()
    {
        // Change the color of the cube
        ChangeCubeColor();

        // Start or stop continuous rotation
        if (!isRotating)
        {
            rotationCoroutine = StartCoroutine(ContinuousRotation());
            isRotating = true;
        }
        else
        {
            StopCoroutine(rotationCoroutine);
            isRotating = false;
        }
    }

    private void ChangeCubeColor()
    {
        // Generate a random color
        Color newCubeColor = Random.ColorHSV();

        // Apply the new color to the cube
        CubeRenderer.material.color = newCubeColor;
    }

    private IEnumerator ContinuousRotation()
    {
        while (true)
        {
            // Rotate the cube around the y-axis
            CubeTransform.Rotate(Vector3.up, 120f * Time.deltaTime);

            yield return null;
        }
    }
}